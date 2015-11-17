#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_Mail import Mail
from formatThesaurus import checkThesaurus, createThesaurus
from formatThesaurus import createThesaurusHardcore
from simpleRequest import *
import os

# Global Variables
rPath = 'ressources/MRCONSO_2011AA.RRF'  # Path to base file
tPath = 'ressources/FormattedThesaurus.RRF'  # Path to formatted file
mPath = 'ressources/mails'  # Path to email files
tSizeHardcore = 6044285  # Expected number of lines in the formatted file
tSize = 6046983  # Use this for Thesaurus with words of length 2
oPath = 'sortie.txt'
hardcordeMode = True

# Setting working directory to path of current file
os.path.dirname(os.path.abspath(__file__))

# Checking if thesaurus exists and is correctly formatted
# If not, create it
if hardcordeMode:
    print('You are in hardcore mode')
    if not checkThesaurus(tPath, tSizeHardcore):
        createThesaurusHardcore(rPath, tPath)
else:
    if not checkThesaurus(tPath, tSize):
        createThesaurus(rPath, tPath)

# Open the new thesaurus and store it in memory
f = open(tPath, encoding='utf-8')
thesaurus = list(f)
f.close()

with open(oPath, 'w', encoding='utf-8') as output_file:
    # Main part: open each email and tag them
    for root, dirs, files in os.walk(mPath, topdown=False):
        for f in files:
            mail = Mail(os.path.join(root, f))
            findEntries(thesaurus, mail, output_file)
