########
*WHATSAPPP PYTHON SCRIPT*

Using `pywhatkit` https://pypi.org/project/pywhatkit/ 

Prerequisites:
- Enable Whatsapp Web

Run with
```
pip install -r requirements.txt
python send.py
```
Tested with Python 3.9

Known issues:
- Whatsapp web takes time to load on cold start. Timeout currently set to 20 seconds - sometimes first message may get skipped if it takes too long. 
-- Workaround: Run whatsapp web with a dummy message beforehand