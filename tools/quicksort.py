#<<qsort1>>=
#source http://en.literateprograms.org/Quicksort_(Python)

import random
import time
import sys



def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater
"""
l2 = []

nb = 100 # numbers to generate

# generate xx numbers to pop a list
for i in range(nb):
    nbal = random.randint(0,10000000)
    l2.append(nbal)

#sort list
l2 = qsort1(l2) 
# display the x % of the set
# n_to_disp = round(nb * 0.05 / 100)
n_to_disp = 100
for i in range (0, n_to_disp, 1):
    print(l2[i])
"""

liste_strings = [] 



nb_lignes = 0

with open(sys.argv[1],'r',encoding='utf-8') as fh:
    start_construct_list = time.time()
    for line in fh:
        liste_strings.append(line)
        nb_lignes += 1
    end_construct_list = time.time()
    start_quicksort = time.time()
    liste_strings = qsort1(liste_strings)
    end_quicksort = time.time()

time_gen_list = end_construct_list - start_construct_list
time_quicksort = end_quicksort - start_quicksort


print("Nb lignes: " + str(nb_lignes))
print("Tps gen liste: " + str(time_gen_list))
print("Tps QS: " + str(time_quicksort))
"""
for i in range (len(liste_strings)):
    print(liste_strings[i])
"""


