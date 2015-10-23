#<<qsort1>>=
#source http://en.literateprograms.org/Quicksort_(Python)

import random
def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

l2 = []

nb = 10000000 # numbers to generate

# generate xx numbers to pop a list
for i in range(nb):
    nbal = random.randint(0,10000000)
    l2.append(nbal)

#sort list
l2 = qsort1(l2) 

# display the x % of the set
n_to_disp = round(nb * 0.05 / 100)
for i in range (0, n_to_disp, 1):
    print(l2[i])

