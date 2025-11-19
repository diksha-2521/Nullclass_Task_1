import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"   # Force CPU to avoid GPU errors

import tkinter as tk
from tkinter import ttk
import json
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing.text import tokenizer_from_json
from keras.utils import pad_sequences


# ----------------------------------------------------------
# Load the French → Tamil model and tokenizers
# ----------------------------------------------------------

# Load model
model = load_model("french_to_tamil_model")

# Load French tokenizer
with open("french_tokenizer.json") as f:
    data = json.load(f)
    french_tokenizer = tokenizer_from_json(data)

# Load Tamil tokenizer
with open("tamil_tokenizer.json") as f:
    data = json.load(f)
    tamil_tokenizer = tokenizer_from_json(data)

# Build index → token dictionary
index_to_tamil = {v: k for k, v in tamil_tokenizer.word_index.items()}

# Load max word length from training
with open("sequence_length.json") as f:
    MAX_LEN = json.load(f)



# ----------------------------------------------------------
# Translation function
# ----------------------------------------------------------
def translate_french_word():
    word = input_box.get().strip().lower()
    output_box.delete("1.0", "end")

    # Only allow 5-letter French words
    if len(word) != 5:
        output_box.insert("end", "Error: Only 5-letter French words are allowed.")
        return

    # Tokenize and pad
    seq = french_tokenizer.texts_to_sequences([word])
    seq = pad_sequences(seq, maxlen=MAX_LEN, padding="post")

    # Predict
    pred = model.predict(seq)
    pred_indices = np.argmax(pred, axis=-1)[0]

    tamil_word = "".join([index_to_tamil.get(i, "") for i in pred_indices]).strip()

    output_box.insert("end", tamil_word)


def copy_output():
    text = output_box.get("1.0", "end").strip()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()


# ----------------------------------------------------------
# GUI Layout
# ----------------------------------------------------------

root = tk.Tk()
root.title("French → Tamil Translator (5-letter words only)")
root.geometry("550x400")

font_style = "Times New Roman"
font_size = 14

# Heading
heading = tk.Label(root, text="French → Tamil Translator", font=(font_style, font_size, "bold"))
heading.pack(pady=10)


# ---- Input section ----
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter a 5-letter French word:", font=(font_style, font_size))
input_label.pack()

input_box = tk.Entry(input_frame, font=(font_style, font_size), width=25)
input_box.pack(pady=5)


# Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_french_word)
translate_button.pack(pady=10)


# ---- Output section ----
output_label = tk.Label(root, text="Tamil Translation:", font=(font_style, font_size, "bold"))
output_label.pack()

output_box = tk.Text(root, height=3, width=50, font=(font_style, font_size))
output_box.pack(pady=5)


# Copy button
copy_button = ttk.Button(root, text="Copy Output", command=copy_output)
copy_button.pack(pady=5)


root.mainloop()
