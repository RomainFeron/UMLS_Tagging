#!/usr/bin/env python
# -*- coding: utf-8 -*-

file1 = 'list_cui_process.txt'
file2 = 'list_cui_process_marked.txt'

def calcul(path):
    fh = open(path, 'r', encoding='utf-8')
    liste = {}
    for line in fh:
        tab = line.split('|')
        cui = tab[0]
        val = tab[1]
        if tab[0] in liste.keys():
            liste[cui].append(val)
        else:
            liste[cui] = [val]

    nb_k = 0
    nb_v = 0
    for key in liste:
        nb_k +=1
        for e in liste[key]:
            nb_v +=1
    print('calcul pour fichier: ', path)
    print('Process : cui uniques | cui total')
    print(nb_k, nb_v)

calcul(file1)
calcul(file2)
