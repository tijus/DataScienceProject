#!/usr/bin/python3


import sys
import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

special = ['amp', 'marchforourlives', 'none', 'i’m', 'th','don’t','it’s','advertisement']

with open('/home/edexworld/Sujit/DIC/Lab2/Part2/lib/seostopwords.txt') as f:
    stopLines = f.read().splitlines()

dump = [stop_words.add(i) for i in special]
dump = [stop_words.add(i) for i in stopLines]


def reg(line):
    line = (re.sub('(RT )*@.+? ', '',line)) # dont want <RT and/or @user> tags
    line = (re.sub('http.+? ', '',line)) # dont want web adresses
    line = re.sub(',', ' ', line)
    line = line.lower()
    words = re.findall('([a-z]+?.{0,1}?[a-z]*?)\W*\s+',line) # regex to extract words (space delmit, remove special chars at end of words)
    return words



for line in sys.stdin:

    line = line.strip()
    word_tokens = reg(line)
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    
    for word in filtered_sentence:
        print(word+"\t"+str(1))

