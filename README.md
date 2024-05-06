# gTranslate
## Overview

Translate the `source.txt` to the target language with Google Translate API.  
Translated output saved to `target.txt` in the same directory.


## Installation
1. Install Google Cloud SDK shell.

2. Install dependent api.
```shell
pip install google-cloud-translate
```
3. Generate API key of service account in Google Cloud, save the json file to local.

4. Replace the `credentials_path` with your local file.
```
credentials_path = "path/to/your/credentials.json"
```

## Example
In Google Clould SDK shel, run 

```bash
C:\GitHub>cd gTranslate

C:\GitHub\gTranslate>c:\ProgramData\Anaconda3\python translate.py
Enter target language (e.g., en, es, fr): es
Translated Text: ¡esto es una manzana! Cómo estás hoy.
Translation saved to 'C:\GitHub\gTranslate\target.txt'
```
