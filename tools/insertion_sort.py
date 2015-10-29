import random as rand
import sysx
import time

source = []
target = []

"""Fournir fichier de travail en argument"""
nb_lignes = 7455837 # dans le TH

with open(sys.argv[1],'r',encoding='utf-8') as fh:
    for line in fh:
        source.append(line)

print("Th charge en memoire")


#procedure de controle avancee
pas = 100
hit = []
for i in range(0, nb_lignes, 100):
    hit.append(i)
def control(l, hit):
    if l in hit:
        print (l)

start = time.time()
while len(source)!=0:
    if len(target) ==0:
        target.append(source[0])
        source.pop(0)
    control(len(target),hit) #affichage quand hit peaks
    if len(target) == 10000:
        end = time.time()
        print("Duree: " + str((end - start)))
        break
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


th_t = open('Thesaurus_trie.RRF', 'w', encoding='utf-8')
for element in target:
    th_t.write(element)

    
    

