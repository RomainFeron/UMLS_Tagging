#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


ressourcesPath = 'ressources'
# Path to formatted thesaurus file
formattedThesaurusPath = os.path.join(ressourcesPath, 'FormattedThesaurus.RRF')
# Setting working directory to path of current file
os.path.dirname(os.path.abspath(__file__))

# Open the new thesaurus and store it in memory
f = open(formattedThesaurusPath, encoding='utf-8')
thesaurus = list(f)
f.close()

l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0

for entry in thesaurus:
    s = len(entry.split('|')[0])
    if s < 10:
        l[0] += 1
    elif s < 20:
        l[1] += 1
    elif s < 30:
        l[2] += 1
    elif s < 40:
        l[3] += 1
    elif s < 50:
        l[4] += 1
    elif s < 60:
        l[5] += 1
    elif s < 70:
        l[6] += 1
    elif s < 80:
        l[7] += 1
    elif s < 90:
        l[8] += 1
    elif s < 100:
        l[9] += 1
    else:
        l[10] += 1
    k += 1

of = open('distrib.txt', 'w', encoding='utf-8')

for i in l:
    of.write(str(i)+',')
