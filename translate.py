from google.cloud import translate_v2 as translate
from google.api_core import exceptions
import os


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





if __name__ == "__main__":
    # Get the script's current directory (for reliable file paths)
    script_dir = os.path.dirname(__file__)

    # File paths - Assume files are in the same directory as this script
    source_file = os.path.join(script_dir, "source.txt")
    target_file = os.path.join(script_dir, "target.txt")

    try:
        # Read text from the input file
        with open(source_file, "r", encoding='utf-8') as f:
            text_to_translate = f.read()

        target_lang = input("Enter target language (e.g., en, es, fr): ")

        translated_text = translate_text(text_to_translate, target_lang)
        print(f"Translated Text: {translated_text}")

        # Write the translated text to the output file
        with open(target_file, "w", encoding='utf-8') as f:
            f.write(translated_text)

        print(f"Translation saved to '{target_file}'")

    except (FileNotFoundError, IOError) as e:
        print(f"Error reading/writing files: {e}")
    except ValueError as e:
        print(f"Error: {e}")
