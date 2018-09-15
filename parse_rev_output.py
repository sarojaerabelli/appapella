#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:07:33 2018

@author: samyu
"""

import json
import pyphen

# TODO: use Rev Python SDK to get the json file

# Parse json into a dictionary
with open('/Users/samyu/Desktop/historyeyesonyou.json') as f:
    data = json.load(f)

# Get syllables from dictionary
lyrics = ""
syllables = []
dic = pyphen.Pyphen(lang='en')
for m in data["monologues"]:
    for e in m["elements"]:
        lyrics += e["value"]
        if e["type"] == "text":
            syllables.extend(dic.inserted(e["value"]).split("-"))

print(lyrics)
print(syllables)
