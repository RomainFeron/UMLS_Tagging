import random as rand
import sys

source = []
target = []

with open(sys.argv[1],'r',encoding='utf-8') as fh:
    for line in fh:
        source.append(line)


while len(source)!=0:
    if len(target) ==0:
        target.append(source[0])
        source.pop(0)
    element = source.pop(0)
    if(element <= target[0]):
        target.reverse()
        target.append(element)
        target.reverse()
    elif element > target[len(target)-1]:
        target.append(element) 
    else:
        for i in range(0,len(target)-1):
            if element >= target[i] and element <= target[i+1]:
                target.insert(i+1,element)
                break

for e in range(len(target)):
    print(target[e])

