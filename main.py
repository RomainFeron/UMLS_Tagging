#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_Mail import Mail
from formatThesaurus import checkThesaurus, createThesaurus, createThesaurusHardcore
import os

# Global Variables
rPath = 'ressources/MRCONSO_2011AA.RRF'  # Path to base file
tPath = 'ressources/FormattedThesaurus.RRF'  # Path to formatted file
mPath = 'ressources/mails'  # Path to email files
tSize = 6044285  # Expected number of lines in the formatted file
# tSize = 6046983 -- Use this for Thesaurus with words of length 2

# Setting working directory to path of current file
os.path.dirname(os.path.abspath(__file__))

# Checking if thesaurus exists and is correctly formatted
# If not, create it
if not checkThesaurus(tPath, tSize):
    createThesaurusHardcore(rPath, tPath)

# Open the new thesaurus and store it in memory
with open(tPath, encoding='utf-8') as f:
    thesaurus = list(f)

# Main part: open each email and tag them
for root, dirs, files in os.walk(mPath, topdown=False):
    for f in files:
        mail = Mail(os.path.join(root, f))
        print(mail.title)
        # placeholder for the function
