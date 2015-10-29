import random
import time
import sys


source = []
with open(sys.argv[1],'r',encoding='utf-8') as fh:
    for line in fh:
        source.append(line)
print("Th charge en memoire")



def qsort2(list):
    """Quicksort using a partitioning function"""
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser, equal, greater = partition(list[1:], [], [pivot], [])
        return qsort2(lesser) + equal + qsort2(greater)

def partition(list, l, e, g):
    while list != []:
        head = list.pop(0)
        if head < e[0]:
            l = [head] + l
        elif head > e[0]:
            g = [head] + g
        else:
            e = [head] + e
    return (l, e, g)



start = time.time()
source = qsort2(source)
end = time.time()

"""
for i in range(0, len(ma_liste)):
    print(ma_liste[i])
"""

print(source)

# print("Temps mis pour le Qsort: " + str(end-start))
