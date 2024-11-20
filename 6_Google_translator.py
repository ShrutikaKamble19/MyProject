from googletrans import Translator

def translate_text(text, target_language):
    """
    Translates a given text to the specified target language.
    
    Parameters:
        text (str): The text to be translated.
        target_language (str): The language code to translate the text into (e.g., 'en' for English, 'fr' for French).
        
    Returns:
        str: Translated text.
    """
    # Initialize the Google Translator
    translator = Translator()

    # Perform the translation
    translation = translator.translate(text, dest=target_language)
    
    # Return the translated text
    return translation.text

# Example usage
text = "Hello, how are you?"
target_language = "es"  # Spanish
translated_text = translate_text(text, target_language)
print(f"Translated text: {translated_text}")
