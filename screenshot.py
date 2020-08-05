import io
import ctypes
import requests
import json
import urllib.parse
import os

from PIL import ImageGrab

im = ImageGrab.grabclipboard()

if not im:
    ctypes.windll.user32.MessageBoxW(0, "No screen shot in clipboard - do win-shift-s, then try again", "Screenshot searcher", 0)
    exit()

store = io.BytesIO()
im.save(store, format="jpeg")
store.seek(0)

files = { 'file': store }
resp = requests.post("https://file.io", files=files)
print(resp.content)

respJson = json.loads(resp.content)
lnk = respJson["link"]

print(lnk)
gSearch = r"https://images.google.com/searchbyimage?image_url=" + urllib.parse.quote_plus(lnk)
os.system("start " + gSearch)