# Nullclass_Task_1

This is project to complete the task of creating  machine learning model and a GUI that translates only 5-letter French words to Tamil


# Overview

This project provides a French-to-Tamil translation system with a strict rule:


Only French words with EXACTLY 5 letters are allowed.

If the input word has fewer or more than 5 letters, the system will not translate it.


The project consists of:

## French_Tamil_Translator.ipynb

A machine learning notebook used to explore and build translation models.
(Not required for GUI execution if using the googletrans version.)


## gui.py

A Tkinter-based desktop GUI.

Uses the previous mentioned model for French to Tamil translation.

Has lesser accuracy than the GUI using googletrans library.


## gui_2.py

Uses googletrans as the translation backend.

Has better accuracy than the French_Tamil_Translator.ipynb model

##
Both the GUIs allow the users to:

Enter a French word and receive a Tamil translation.

Copy translated text using the "Copy Output button.


# Features

✔ Translates 5-letter French words into Tamil

✔ Rejects invalid input (words not exactly 5 letters)

✔ Clean Tkinter graphical interface

✔ Copyable output field

✔ Uses Google Translate API (via googletrans)


# Requirements

Before running the gui.py file make to install the required library using the following command:

``` pip install googletrans==4.0.0-rc1 ```

# About French_Tamil_Translator.ipynb
In this notebook we use the dataset from <a href='https://opus.nlpl.eu/XLEnt/fr&ta/v1.2/XLEnt'> https://opus.nlpl.eu/XLEnt/fr&ta/v1.2/XLEnt<a> for training a Biredirectional Embedding model. 

The reason for choosing this dataset is that it is the only dataset I found that contained a lot of five letter French word. (Although the ratio of them is very low hence the lower accuracy.)

As the translation is of such a small scale I used Biredirectional Embedding model instead of a heavy duty Positional Embedding model that requires many attention layers. 

The trained weights of the model, both the languages tokenizers and the sequence length of the model are saved in french_to_tamil_model and json files respectively.


# About the GUIs

The GUI contains:


An input field

A translate button

A Tamil output area

A "Copy Output" button

## How to Use

1. Type a French word with exactly 5 letters.
Example:

pomme


2. Click Translate.

3. The translated Tamil word appears in the output area.

4. Click Copy Output to copy the Tamil text to your clipboard.

If the word is NOT 5 letters long, the GUI shows:

``` Error: Only 5-letter French words are allowed. ```

# Notes & Limitations

## Googletrans reliability

The googletrans library relies on unofficial Google endpoints.

Translations may occasionally fail due to:

* API rate limits

* Network issues

* Changes in Google Translate’s backend

The GUI includes proper error handling to display helpful messages instead of crashing.

## Unreliable accuracy of the created model

The French_Tamil_Translator.ipynb model has trained on a very small dataset of almost 15,000 entries. 

This makes the model prone to overfitting and having overall lesser accuracy.

# Future Improvements

* Using a larger dataset to improve the accuracy of the model created.

# Author

This project was developed to fulfill the requirement:

"Create a machine learning feature and GUI that translates French 5-letter words into Tamil."
