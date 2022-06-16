#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import csv
import json
import timestamp as custom_Word

SetLogLevel(0)

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)

n = sys.argv[1] 
path = './textfiles/' + n[9:-4] + '.csv'
f = open(path,'w',encoding = 'UTF_8_sig')
writer = csv.writer(f)

wf = open(sys.argv[1], "rb")
wf.read(44) # skip header


resulttext = []
model = Model("model")
rec = KaldiRecognizer(model, 16000)
rec.SetWords(True)
##rec.SetPartialWords(True)

# get the list of JSON dictionaries
results = []
# recognize speech using vosk model
while True:
    data = wf.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        part_result = json.loads(rec.Result())
        results.append(part_result)
part_result = json.loads(rec.FinalResult())
results.append(part_result)

# convert list of JSON dictionaries to list of 'Word' objects
list_of_Words = []
a = 0
for sentence in results:
    if len(sentence) == 1:
        # sometimes there are bugs in recognition 
        # and it returns an empty dictionary
        # {'text': ''}
        continue
    for obj in sentence['result']:
        w = custom_Word.Word(obj)
        if a == 0:
            writer.writerow([w.start,sentence['text']])
            a = 1
    a = 0
        
        
wf.close() 
