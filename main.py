#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UMLS tagging tool by Issa Diop, Romain Feron and Wilfried Poudroux.
Version 1.0 (2015-12-06)
Find out more on github: http://github.com/RomainFeron/UMLS_tagging
"""

import os
from multiprocessing.dummy import Pool as ThreadPool
from formatThesaurus import *
from request import *
from class_Mail import Mail


# Parallelisation of request function
def parallelTagging(mailPath, thesaurus, outputPath):

    mail = Mail(mailPath)
    print('Tagging mail : ' + mail.title)
    findEntries(thesaurus, mail, outputPath)

# Global variables
ressourcesPath = 'ressources'
# Path to base thesaurus file
originalThesaurusPath = os.path.join(ressourcesPath, 'MRCONSO_2011AA.RRF')
# Path to formatted thesaurus file
formattedThesaurusPath = os.path.join(ressourcesPath, 'FormattedThesaurus.RRF')
# Path to email files
mailsPath = os.path.join(ressourcesPath, 'mails')
# Path to output folder
outputPath = 'output'
# Expected number of lines in the formatted file (non conservative)
tSizeNonConservative = 6044285
# Expected number of lines in the formatted file (conservative)
tSize = 6046983  # Use this for Thesaurus with words of length 2
# Set this to 'True' if you want to tag words of length 2
conservative = False

# Setting working directory to path of current file
os.path.dirname(os.path.abspath(__file__))

# Check if thesaurus exists and is correctly formatted according to the
# mode chosen (conservative or not conservative). If not, create it
if not conservative:
    print('You are in non-conservative mode')
    if not checkThesaurus(formattedThesaurusPath, tSizeNonConservative):
        createThesaurus_nc(originalThesaurusPath, formattedThesaurusPath)
else:
    print('You are in conservative mode')
    if not checkThesaurus(formattedThesaurusPath, tSize):
        createThesaurus_c(originalThesaurusPath, formattedThesaurusPath)

# Open the new thesaurus and store it in memory
f = open(formattedThesaurusPath, encoding='utf-8')
thesaurus = list(f)
f.close()

# Create the list of arguments for parallel function
# Arguments : path to email, thesaurus, path to output file
mailsList = []
for root, dirs, files in os.walk(mailsPath, topdown=False):
    for f in files:
        temp = [os.path.join(root, f), thesaurus, outputPath]
        mailsList.append(temp)

# Parallel baby
pool = ThreadPool()
results = pool.starmap(parallelTagging, mailsList)
