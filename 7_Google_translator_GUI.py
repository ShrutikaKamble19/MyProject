from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, Text, END
from googletrans import Translator

def translate_text():
    """
    Translates the user-input text to the selected target language and displays the result.
    """
    # Get text and target language from the user
    text = input_text.get("1.0", END).strip()
    target_language = language_var.get()
    
    # Check if input is valid
    if not text:
        result_label.config(text="Please enter some text to translate.")
        return
    if not target_language:
        result_label.config(text="Please select a target language.")
        return

    # Perform translation
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        translated_text = translation.text
        result_label.config(text=f"Translated text: {translated_text}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Initialize the Tkinter app
app = Tk()
app.title("Text Translator")
app.geometry("400x400")

# Input Text Label and Text Box
Label(app, text="Enter text to translate:", font=("Arial", 12)).pack(pady=10)
input_text = Text(app, height=5, width=40, wrap="word", font=("Arial", 10))
input_text.pack(pady=5)

# Language Selection
Label(app, text="Select target language:", font=("Arial", 12)).pack(pady=10)
language_var = StringVar()
language_var.set("")  # Default value (empty)
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Hindi": "hi",
}
language_menu = OptionMenu(app, language_var, *languages.values())
language_menu.pack(pady=5)

# Translate Button
Button(app, text="Translate", command=translate_text, font=("Arial", 12)).pack(pady=20)

# Result Label
result_label = Label(app, text="", font=("Arial", 12), wraplength=350, justify="center")
result_label.pack(pady=20)

# Run the app
app.mainloop()
