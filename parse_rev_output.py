#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 14:07:33 2018

@author: samyu
"""

import pyphen
import requests
import time

API_KEY = "Bearer 01s3z3zuFg7UIPaZD6chbx-L7XDanknk-dK95e0ARlIRG5q1Gj2qZICGXeCj1hKlKq0-Rpytz3WJdRloLIEyJ37Ige2sM"
HEADERS = {'Authorization': API_KEY}

def submit_job(media_url, metadata):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    payload = {'media_url': media_url,
               'metadata': metadata}
    request = requests.post(url, headers=HEADERS, json=payload)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']

def view_job(id):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
    request = requests.get(url, headers=HEADERS)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def get_transcript(id):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript'
    headers = HEADERS.copy()
    headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def submit_and_transcribe(url, metadata):
    print ("Submitting job")
    job_id = submit_job(url, metadata)
    print ("Job created")
    view_job(job_id)

    while True:
        job = view_job(job_id)
        status = job["status"]
        print(f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(job_id)

def parse_lyrics(json_data):
    # Parse json into a dictionary
    #data = json.load(json_data)
    
    # Get syllables from dictionary
    lyrics = ""
    syllables = []
    dic = pyphen.Pyphen(lang='en')
    for m in json_data["monologues"]:
        for e in m["elements"]:
            lyrics += e["value"]
            if e["type"] == "text":
                s = dic.inserted(e["value"]).split("-")
                if len(s) == 1:
                    syllables.append(("single", s[0]))
                else:
                    syllables.append(("begin", s[0]))
                    for i in range(1, len(s) - 1):
                        syllables.append(("middle", s[i]))
                    syllables.append(("end", s[-1]))
    return (lyrics, syllables)

def main():
    media_url = ("https://dl.dropboxusercontent.com/s/io3v"
                 "6qtbf9hux35/2-23%20Who%20Lives%2C%20Who%20Dies%2C%20Who"
                 "%20Tells%20Your%20Story.m4a")
    
    l, s = parse_lyrics(submit_and_transcribe(media_url, "WhoLivesWhoDies"))
    print(l)
    print(s)

if __name__ == "__main__":
    main()