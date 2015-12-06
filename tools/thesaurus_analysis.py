#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


# Global variables
ressourcesPath = 'ressources'
# Path to base thesaurus file
originalThesaurusPath = os.path.join(ressourcesPath, 'MRCONSO_2011AA.RRF')

# Path to formatted thesaurus file
formattedThesaurusPath = os.path.join(ressourcesPath, 'FormattedThesaurus.RRF')

# Setting working directory to path of current file
os.path.dirname(os.path.abspath(__file__))

# Open the new thesaurus and store it in memory
f = open(formattedThesaurusPath, encoding='utf-8')
thesaurus = list(f)
f.close()

"""
lang = {}
for line in thesaurus:
    if line.split('|')[1] in lang:
        lang[line.split('|')[1]] += 1
    else:
        lang[line.split('|')[1]] = 0

o = open('lang_Analysis.txt', 'w', encoding='utf-8')
for key in lang:
    o.write(key + ', ')
o.write('\n')
for key in lang:
    o.write(str(lang[key]) + ', ')
"""

size = []
k = 0

for line in thesaurus:
    size.append(len(line))
    k += 1

print(sum(size)/k)
