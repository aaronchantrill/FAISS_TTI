# -*- coding: utf-8 -*-
import faiss
import logging
import numpy as np
import os
import re
from naomi import paths
from naomi import plugin
from naomi import profile
from sentence_transformers import SentenceTransformer

# Convert a word ("word") to a keyword ("{word}")
def to_keyword(word):
    return "{}{}{}".format("{", word, "}")


class FAISS_TTIPlugin(plugin.TTIPlugin):
    def __init__(self, *args, **kwargs):
        self._logger = logging.getLogger(__name__)
        self.texts = []
        self.intents = []

    def add_intents(self, intents):
        locale = profile.get("language", "en-US")
        # {'HackerNewsIntent': {'locale': {'en-US': {'keywords': {'NewsKeyword': ['news', 'headlines']}, 'templates': ['read hacker {NewsKeyword}', 'read me hacker {NewsKeyword}', 'tell me the hacker {NewsKeyword}', 'what is in the hacker {NewsKeyword}', 'what is happening in hacker {NewsKeyword}', "what are today's hacker {NewsKeyword}"]}, 'fr-FR': {'templates': ['LISEZ LES NOUVELLES DES HACKERS', 'CE QUI EST DANS LES NOUVELLES HACKER', 'QUELLES SONT LES TITRES DE NOUVELLES HACKER']}, 'de-DE': {'templates': ['HACKER NEWS LESEN', 'WAS IST IN HACKER NEWS', 'WAS SIND DIE HACKER NEWS HEADLINES']}}, 'action': <bound method HackerNewsPlugin.handle of <hn_1_0_0.hackernews.HackerNewsPlugin object at 0x7fbd3dbc9050>>, 'allow_llm': True}}
        for intent in intents:
            if locale not in intents[intent]['locale']:
                raise KeyError("Language not supported")
            for template in intents[intent]['locale'][locale]['templates']:
                self.intents.append(intents[intent]['action'])
                self.texts.append(template)

    def train(self):
        # Load embedding model
        self.model = SentenceTransformer("sentence-transformers/nli-mpnet-base-v2")

        # Compute embeddings
        embeddings = self.model.encode(self.texts, convert_to_numpy=True, normalize_embeddings=True)

        # Create FAISS index (cosine = inner product on normalized vectors)
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dimension)
        self.index.add(embeddings)

        self.trained = True

    def get_plugin_phrases(self, passive_listen=False):
        phrases = []
        # Include any custom phrases (things you say to Naomi
        # that don't match plugin phrases). Otherwise, there is
        # a high probability that something you say will be
        # interpreted as a command. For instance, the
        # "check_email" plugin has only "EMAIL" and "INBOX" as
        # standard phrases, so every time I would say
        # "Naomi, check email" Naomi would hear "NAOMI SHUT EMAIL"
        # and shut down.
        custom_standard_phrases_file = paths.data(
            "standard_phrases",
            "{}.txt".format(profile.get(['language'], 'en-US'))
        )
        if os.path.isfile(custom_standard_phrases_file):
            with open(custom_standard_phrases_file, mode='r') as f:
                for line in f:
                    phrase = line.strip()
                    if phrase:
                        phrases.append(phrase.upper())
        phrases.extend([text.upper() for text in self.texts])
        return sorted(phrases)

    def determine_intent(self, phrase):
        phrase = self.cleantext(phrase)
        query_vector = self.model.encode([phrase], convert_to_numpy=True, normalize_embeddings=True)
        scores, indices = self.index.search(query_vector, 1)
        results = dict()
        for idx, score in zip(indices[0], scores[0]):
            if score < 0.50:
                results["unclear"] = {
                    "action": None,
                    "input": phrase,
                    "matches": "",
                    "score": float(score),
                    "allow_llm": True
                }
            else:
                results[idx] = {
                    "action": self.intents[idx],
                    "input": phrase,
                    "matches": self.texts[idx],
                    "score": float(score),
                    "allow_llm": True
                }
        return results
