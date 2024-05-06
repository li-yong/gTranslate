# gTranslate
## Overview

Translate the `source.txt` to the target language with Google Translate API.  
Translated output saved to `target.txt` in the same directory.


## Installation

1. Install dependent api.
```shell
pip install google-cloud-translate
```
2. Generate API key of service account in Google Cloud, save the json file to local.

3. Replace the `credentials_path` with your local file.
```
credentials_path = "path/to/your/credentials.json"
```

## Example
```bash
$ cat source.txt

this is an Apple!

How are you today.



$ c:\ProgramData\Anaconda3\python translate.py

have read the text from source.txt

Enter target language (e.g., en, es, fr,zh-CN): zh-CN

Translated Text: 这是苹果！你今天好吗？

Translation saved to 'target.txt'



$ cat target.txt

这是苹果！你今天好吗？
```
