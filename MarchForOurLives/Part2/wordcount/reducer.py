#!/usr/bin/python3
import sys
import operator

d = {}
for line in sys.stdin:
    
    # deleting starting and trailing space
    line = line.strip()
    
    words,count = line.split("\t",1)
    count = int(count)
    if d.get(words)==None:
        d[words] = count
    else:
        d[words]=d[words]+count

sorted_d = sorted(d.items(), key=operator.itemgetter(1))

for item in reversed(sorted_d):
    print(item[0]+"\t"+str(item[1]))
    
    

