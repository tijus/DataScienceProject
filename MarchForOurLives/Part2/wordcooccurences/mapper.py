#!/usr/bin/python3

import sys
import re
from nltk.corpus import stopwords
import pandas as pd

stop_words = set(stopwords.words('english'))
special = ['amp', 'marchforourlives', 'none', 'i’m', 'th', 'advertisement']

with open('/home/edexworld/Sujit/DIC/Lab2/Part2/lib/seostopwords.txt') as f:
    stopLines = f.read().splitlines()

dump = [stop_words.add(i) for i in special]
dump = [stop_words.add(i) for i in stopLines]

dfReducer = pd.read_csv('/home/edexworld/Sujit/DIC/Lab2/Part2/visualizations/js/articles.tsv', sep='\t')
# dfReducer = pd.read_csv('nyt.tsv', sep='\t') # use this for consdiering top words from articles

pairs = set()

# make pairs
def make_pairs(df):

    for i in range(len(df)):
        for j in range(i+1,len(df)):
            #print(df.iloc[i][0],df.iloc[j][0])
            pairs.add((df.iloc[i][0],df.iloc[j][0]))

top_count = 10 # no of words to be considered with max freq
make_pairs(dfReducer[0:top_count])
#print(pairs)

def reg (line):
    line = (re.sub('(RT )*@.+? ', '',line)) # dont want <RT and/or @user> tags
    line = (re.sub('http.+? ', '',line)) # dont want web adresses
    line = re.sub(',', ' ', line)
    line = line.lower()
    words = re.findall('([a-z]+?.{0,1}?[a-z]*?)\W*\s+',line) # regex to extract words (space delmit, remove special chars at end of words)
    return words
#reg(Tooter)

for line in sys.stdin:

    line = line.strip()
    word_tokens = reg(line)
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    for pr in pairs:
        if(pr[0] in filtered_sentence and pr[1] in filtered_sentence):
            print(pr[0] + "\t" + pr[1] + "\t" +str(1))



