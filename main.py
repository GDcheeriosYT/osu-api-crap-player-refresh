from importlib.metadata import metadata
import time
import json
from flask import jsonify
import requests
import subprocess
import os
import atexit

def exit_handler():
    requests.post(f"http://gdcheerios.com/api/live/del/{id}")

atexit.register(exit_handler)

with open("id.txt", "r") as f:
  id = f.read()

print("https://github.com/l3lackShark/gosumemory")
print("I use this for data reading, so thanks to him")

os.startfile("gosumemory.exe")

time.sleep(5)

while True:
  info = requests.get("http://127.0.0.1:24050/json").json()
  if info['menu']['state'] != 2 and info['menu']['state'] != 7:
    important_info = {}
    important_info["mapInfo"] = {"background" : f"https://assets.ppy.sh/beatmaps/{info['menu']['bm']['set']}/covers/cover.jpg","metadata" : info['menu']['bm']['metadata'],"stats" : info['menu']['bm']['stats'],"mods" : info['menu']['mods']["str"]}
    important_info["state"] = info['menu']['state']
    important_info["gameplay"] = {"score" : info['gameplay']['score'],"accuracy" : info['gameplay']['accuracy'],"combo" : info['gameplay']['combo']['current'], "grade":info["gameplay"]["hits"]["grade"]["current"]}
    requests.post(f"http://gdcheerios.com/api/live/update/{id}", json=important_info)
    time.sleep(1)
  elif info['menu']['state'] == 7:
    requests.get(f"http://gdcheerios.com/refresh/{id}")
    important_info = {}
    important_info["mapInfo"] = {"background" : f"https://assets.ppy.sh/beatmaps/{info['menu']['bm']['set']}/covers/cover.jpg","metadata" : info['menu']['bm']['metadata'],"stats" : info['menu']['bm']['stats'],"mods" : info['menu']['mods']["str"]}
    important_info["state"] = info['menu']['state']
    important_info["gameplay"] = {"score" : info['gameplay']['score'],"accuracy" : info['gameplay']['accuracy'],"combo" : info['gameplay']['combo']['current'], "grade":info["gameplay"]["hits"]["grade"]["current"]}
    requests.post(f"http://gdcheerios.com/api/live/update/{id}", json=important_info)
    time.sleep(6)
  else:
    important_info = {}
    important_info["mapInfo"] = {"background" : f"https://assets.ppy.sh/beatmaps/{info['menu']['bm']['set']}/covers/cover.jpg","metadata" : info['menu']['bm']['metadata'],"stats" : info['menu']['bm']['stats'],"mods" : info['menu']['mods']["str"]}
    important_info["state"] = info['menu']['state']
    important_info["gameplay"] = {"score" : info['gameplay']['score'],"accuracy" : info['gameplay']['accuracy'],"combo" : info['gameplay']['combo']['current'], "grade":info["gameplay"]["hits"]["grade"]["current"]}
    requests.post(f"http://gdcheerios.com/api/live/update/{id}", json=important_info)
    time.sleep(0.35)