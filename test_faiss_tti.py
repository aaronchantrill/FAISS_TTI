# -*- coding: utf-8 -*-
import unittest
from naomi import testutils
from . import faiss_tti


class TestFAISS_TTIPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = testutils.get_plugin_instance(faiss_tti.FAISS_TTIPlugin)
