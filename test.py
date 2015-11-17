#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Global Variables
rPath = 'ressources/MRCONSO_2011AA.RRF'  # Path to base file
tPath = 'ressources/FormattedThesaurus.RRF'  # Path to formatted file


formattedThesaurus = open(tPath, 'r', encoding='utf-8')
forbidden = ['[']
ft = []
k=0
for line in formattedThesaurus:
    k+=1
print(k)
