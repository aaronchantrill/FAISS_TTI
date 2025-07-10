---
id: FAISS_TTI
label: FAISS TTI
title: FAISS Text to Intent
type: tti
description: "Allows Naomi to use FAISS for intent parsing"
source: https://github.com/aaronchantrill/FAISS_TTI/blob/main/readme.md
meta:
  - property: og:title
    content: "FAISS TTI - Text to Intent"
  - property: og:description
    content: "Allows Naomi to use FAISS for intent parsing"
---

# FAISS TTI - Text to Intent


To install a plugin in Naomi, you can follow the instructions below.

# FAISS TTI Plugin for Naomi

## Overview

The **FAISS TTI** Plugin is a powerful natural language understanding (NLU) component designed for the Naomi platform. It uses Facebook AI Similarity Search to interpret spoken language commands and map them to intents. This plugin enhances Naomi’s ability to process user input using a trained neural network model, enabling highly accurate intent classification.

The plugin’s primary function is to analyze user speech, identify intents through text-to-intent (TTI) recognition, and return relevant actions based on installed intents. This makes it an integral part of voice-controlled applications, allowing Naomi to become a more intelligent and adaptive voice assistant.

## Key Features

- **Efficient Intent Recognition**: Leverages FAISS, a vector based meaning similarity engine, to understand user commands and associate them with the appropriate responses or actions.
- **Training and Customization**: Supports training new intents from user input, making it flexible to adapt to different use cases and commands.
- **Seamless Integration**: Fully compatible with the Naomi platform, allowing easy integration into existing voice-controlled setups.
- **Multilingual Support**: Offers the ability to support multiple languages depending on the training data provided.
- **Lightweight and Fast**: Designed to run efficiently even on low-resource devices while maintaining high accuracy for intent classification.

## Requirements

### Python Requirements:
- `faiss`

These dependencies ensure that the necessary libraries and tools for neural network training and intent recognition are properly set up.

## Installation

1. **Clone the Repository**: Clone the FAISS TTI plugin repository from GitHub:
   ```bash
   git clone https://github.com/aaronchantrill/FAISS_TTI.git
   ```

2. **Install Required Dependencies**: Install the necessary packages by running:
   ```bash
   workon Naomi
   pip install faiss
   ```

3. **Add to Naomi Configuration**: Once installed, configure the plugin within the Naomi framework by updating the plugin directory with the path to the FAISS TTI plugin.

### Plugin Installation in Naomi

You can also use Naomi to automatically install this plugin:

```bash
$ Naomi --list-available-plugins
```

This will give you a list of available plugins, for example:

```plaintext
Available Plugins:
Announcements (notificationclient [1.0.0 installed]) - Naomi makes announcements at scheduled times.
Archive Audiolog (stt_trainer [1.0.0]) - Allows the user to export their audiolog database and audio files into an archive file that can be merged into a different Naomi using the Import Audiolog plugin.
...
FAISS TTI (tti [0.1.0]) - Allows Naomi to use FAISS for intent parsing
```

Then use a command like:

```bash
$ Naomi --install "FAISS TTI"
```

to actually install the plugin.

## Usage

To use this plugin, either use `Naomi --repopulate` to run the wizard and select this Text to Intent engine, or edit the profile.yml file file directly:
```
tti_engine: FAISS TTI
```

## Contributing

Contributions are welcome! If you would like to contribute to the development of this plugin, feel free to open a pull request on GitHub. Ensure that your code follows the project’s guidelines and includes appropriate test cases.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Add your changes, and ensure all tests pass.
4. Open a pull request with a clear description of your changes.

## License

This plugin is licensed under the MIT License. See the LICENSE file for more details.

## Example Usage in Naomi

Once installed and configured, the FAISS TTI Plugin enables Naomi to recognize natural language commands. For instance, when a user says:

- **User**: “Turn off the porch light.”
- **Naomi**: Recognizes the ‘turn off the porch light’ intent and sends a signal to the connected home automation system to turn off the light.

This plugin plays a crucial role in making Naomi’s interactions more natural and intuitive for users, whether it’s for smart home control, entertainment systems, or general voice-command tasks.

This detailed description includes the process of listing available plugins and installing the **FAISS TTI** plugin within Naomi.
