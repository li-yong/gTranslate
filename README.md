# gTranslate
## Overview

Translate the `source.txt` to the target language with Google Translate API.  
Translated output saved to `target.txt` in the same directory.

## Installation
**Step 1: Install Python**

If you don't already have Python installed on your system, download and install it from the official Python website: 

**Step 2: Install Required Libraries**

The script uses the `google-cloud-translate` library, which requires the `google-api-python-client` library. Install these libraries using pip:
```
pip install google-cloud-translate google-api-python-client
```
**Step 3: Set up Google Cloud Account and Enable Translation API**

To use the Google Cloud Translation API, you need to:

1. Create a Google Cloud account if you don't already have one.
2. Enable the Google Cloud Translation API for your project. You can do this by going to the Google Cloud Console, navigating to the API Library page, and clicking on "Enable" next to the "Cloud Translation API" entry.
3. Create a service account and generate a private key file (JSON key file). You can do this by going to the IAM & Admin > Service accounts page, creating a new service account, and then generating a key file.

**Step 4: Save the JSON Key File**

Save the JSON key file to a secure location on your system. In the script, replace the `credentials_path` variable with the path to your JSON key file.

**Step 5: Create Source and Target Files**

Create two text files, `source.txt` and `target.txt`, in the same directory as the script. These files will be used to store the original text and the translated text, respectively.

**Step 6: Run the Script**

Run the script using Python:
```
python translate_script.py
```
The script will prompt you to enter the target language (e.g., en, es, fr). Enter the language code, and the script will translate the text in `source.txt` to the specified language and save the translated text to `target.txt`.

**Troubleshooting**

If you encounter any errors while running the script, check the following:

* Make sure you have the correct path to your JSON key file in the `credentials_path` variable.
* Ensure that you have enabled the Google Cloud Translation API for your project.
* Check that you have the correct language code for the target language.
* Verify that the `source.txt` and `target.txt` files are in the same directory as the script.


## Example
In Google Clould SDK shel, run 

```bash
C:\GitHub>cd gTranslate

C:\GitHub\gTranslate>c:\ProgramData\Anaconda3\python translate.py
Enter target language (e.g., en, es, fr): es
Translated Text: ¡esto es una manzana! Cómo estás hoy.
Translation saved to 'C:\GitHub\gTranslate\target.txt'
```
