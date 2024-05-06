# gTranslate
## Overview

Translate the `source.txt` to the target language with Google Translate API.  
Translated output saved to `target.txt` in the same directory.


## Installation

```shell
pip install google-cloud-translate
```

## Example
```bash
$ cat source.txt

this is an Apple!

How are you today.



$ c:\ProgramData\Anaconda3\python b.py

have read the text from source.txt

Enter target language (e.g., en, es, fr,zh-CN): zh-CN

Translated Text: 这是苹果！你今天好吗？

Translation saved to 'target.txt'

$ cat target.txt

这是苹果！你今天好吗？
```
