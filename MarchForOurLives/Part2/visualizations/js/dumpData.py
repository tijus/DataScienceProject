#!/usr/bin/python3

import json
data=[]
with open('output.json', 'w') as outfile,open("tweets.tsv","r") as f:
    for line in f:
       sp=line.split()
       data.append({"Word":sp[0],"Count":sp[1]})
    json.dump(data,outfile)
#print(output)
