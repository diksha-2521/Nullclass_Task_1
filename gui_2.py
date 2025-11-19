import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Initialize the Google translator
translator = Translator()


# ----------------------------------------------------------
# Translation function
# ----------------------------------------------------------
def translate_french_word():
    french_word = input_box.get()

    # Clear previous output
    output_box.delete("1.0", "end")

    # Check if the word has exactly 5 letters
    if len(french_word.strip()) != 5:
        output_box.insert("end", "Error: Only 5-letter French words are allowed.")
        return

    try:
        # Translate using googletrans (source=fr, dest=ta)
        result = translator.translate(french_word, src='fr', dest='ta')
        tamil_translation = result.text

        output_box.insert("end", tamil_translation)

    except Exception as e:
        output_box.insert("end", f"Translation error: {str(e)}")


# ----------------------------------------------------------
# Copy translation to clipboard
# ----------------------------------------------------------
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
