#!/usr/bin/python3
import sys
import operator

d = {}
for line in sys.stdin:

    # deleting starting and trailing space
    line = line.strip()

    word1,word2,count = line.split("\t",2)
    count = int(count)
    words = word1+","+word2
    if d.get(words) == None:
        d[words] = count
    else:
        d[words]=d[words]+count

sorted_d = sorted(d.items(), key=operator.itemgetter(1))

for item in reversed(sorted_d):
    print(item[0]+"\t"+str(item[1]))
