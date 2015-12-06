#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re


# Global variables
ressourcesPath = 'ressources'
# Path to base thesaurus file
originalThesaurusPath = os.path.join(ressourcesPath,'MRCONSO_2011AA.RRF')
# Path to formatted thesaurus file
formattedThesaurusPath = os.path.join(ressourcesPath,'FormattedThesaurus.RRF')
# Path to email files
mailsPath = os.path.join(ressourcesPath,'mails')
# Path to output folder
outputPath = 'output'
tSizeHardcore = 6044285  # Expected number of lines in the formatted file
tSize = 6046983  # Use this for Thesaurus with words of length 2
hardcordeMode = True # Use this if you don't want words of length 2

# Setting working directory to path of current file
os.path.dirname(os.path.abspath(__file__))

# Open the new thesaurus and store it in memory
f = open(formattedThesaurusPath, encoding='utf-8')
thesaurus = list(f)
f.close()

CUI = 'C1449655'

for line in thesaurus:
    if (re.search(CUI, line, re.IGNORECASE)):
        print(line)

