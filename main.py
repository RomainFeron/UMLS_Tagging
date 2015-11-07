#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_Mail import Mail
from formatThesaurus import checkThesaurus, createThesaurus
import os

# Global Variables
rPath = 'ressources/MRCONSO_2011AA.RRF'  # Path to base file
tPath = 'ressources/FormattedThesaurus.RRF'  # Path to formatted file
mPath = 'ressources/mails'
tSize = 6046983  # Expected number of lines in the formatted file

# Setting working directory to path of current file
os.chdir(os.path.dirname(__file__))

# Checking if thesaurus exists and is correctly formatted
# If not, create it
if not checkThesaurus(tPath, tSize):
    createThesaurus(rPath, tPath)

# Main part: open each email and tag them
for root, dirs, files in os.walk(mPath, topdown=False):
    for f in files:
        print(os.path.join(root, f))
        mail = Mail(os.path.join(root, f))
        # placeholder for the function
