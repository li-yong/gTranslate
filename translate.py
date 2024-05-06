from google.cloud import translate_v2 as translate
from google.api_core import exceptions


# Replace with your downloaded JSON key file path
credentials_path = "path/to/your/credentials.json"
translate_client = translate.Client.from_service_account_json(credentials_path)

def translate_text(text, target_language):
  """Translates text to the specified target language."""
  if not text:
    raise ValueError("Text cannot be empty")

  # Check if the target language is supported by the API
  supported_languages = translate_client.get_languages()
  supported_lang_codes = [lang['language'] for lang in supported_languages]

  if target_language not in supported_lang_codes:
    raise ValueError(f"Target language '{target_language}' is not supported by the API.")

  # Attempt to translate
  try:
    result = translate_client.translate(text, target_language=target_language)
    # Decode the translated text from UTF-8 bytes to string
    # translated_text = codecs.decode(result["translatedText"], 'UTF-8')
    translated_text = result["translatedText"]
    return translated_text
  except exceptions.GoogleAPIError as err:
    raise ValueError(f"Translation failed: {str(err)}") from err

# Get user input (same as before)
# text_to_translate = input("Enter text to translate: ")
# Read the text to translate from the input file
with open('source.txt', 'r', encoding='utf-8') as file:
    text_to_translate = file.read()
print("have read the text from source.txt")

target_lang = input("Enter target language (e.g., en, es, fr,zh-CN): ")

# Translate the text with exception handling
try:
    translated_text = translate_text(text_to_translate, target_lang)
    print(f"Translated Text: {translated_text}")

    # Write the translated text to the output file
    with open('target.txt', 'w', encoding='utf-8') as file:
        file.write(translated_text)

    print(f"Translation saved to 'target.txt'")
except ValueError as e:
    print(f"Error: {e}")
