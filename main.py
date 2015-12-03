#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from formatThesaurus import checkThesaurus, createThesaurus
from formatThesaurus import createThesaurusHardcore
from simpleRequest import *
import os
from class_Mail import Mail


# Parallelisation of the program
def parallelTagging(mailPath, thesaurus, outputPath):

    mail = Mail(mailPath)
    findEntries(thesaurus, mail, outputPath)

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

# Checking if thesaurus exists and is correctly formatted
# If not, create it
if hardcordeMode:
    print('You are in hardcore mode')
    if not checkThesaurus(formattedThesaurusPath, tSizeHardcore):
        createThesaurusHardcore(originalThesaurusPath, formattedThesaurusPath)
else:
    if not checkThesaurus(formattedThesaurusPath, tSize):
        createThesaurus(originalThesaurusPath, formattedThesaurusPath)

# Open the new thesaurus and store it in memory
f = open(formattedThesaurusPath, encoding='utf-8')
thesaurus = list(f)
f.close()

# Creates the list of arguments for parallel function
mailsList = []
for root, dirs, files in os.walk(mailsPath, topdown=False):
    for f in files:
        temp = [os.path.join(root, f), thesaurus, outputPath]
        mailsList.append(temp)

# Parallel baby
pool = ThreadPool()
results = pool.starmap(parallelTagging,mailsList)

