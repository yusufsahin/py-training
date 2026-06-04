import os
import sys
import datetime
import json
import socket
import pprint


#Python dili        → if, for, class, def, try/except
#Standard Library   → os, sys, datetime, json, socket, configparser


print("Merhaba")
x =input("Adınız: ")

print(x)

data = {
    "user": {
        "name": "Yusuf",
        "skills": ["Python", "Linux", "PostgreSQL"],
        "settings": {
            "theme": "dark",
            "language": "tr"
        }
    }
}

print(data)

from pprint import pprint

pprint(data)

import os

print(os.getcwd())

import os

os.makedirs("logs", exist_ok=True)

import sys

print(sys.version)
print(sys.platform)

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host = config["database"]["host"]
name= config["database"]["name"]
port = config["database"].getint("port")
debug = config["app"].getboolean("debug")

print(host)
print(port)
print(debug)
print(name)

from datetime import datetime

start = datetime(2026, 6, 1, 10, 0)
end = datetime(2026, 6, 4, 15, 30)

diff = end - start
print(diff)
print(diff.days)
print(diff.total_seconds())

import platform

print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())
print(platform.python_version())

import platform

if platform.system() == "Windows":
    print("Windows ortamı")
elif platform.system() == "Linux":
    print("Linux ortamı")
else:
    print("Diğer işletim sistemi")



import json

data = {"name": "John", "age": 35}

text = json.dumps(data)
print(text)

again = json.loads(text)
print(again["name"])

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Uygulama başladı")
logging.warning("Bu bir uyarı")
logging.error("Bu bir hata")