#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from class_Mail import Mail



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


f = open(formattedThesaurusPath, encoding='utf-8')
thesaurus = list(f)
f.close()


def verifyEntryIsWord(clef, text, pos):
    okChar = [' ', '.', ',', ';', ':']
    if clef in text:
        if pos - 1 > 0 and pos + len(clef) + 1 <= len(text):
            if text[pos - 1] == " " and text[pos + len(clef)] in okChar:
                return(True)
    return(False)


def findEntryInText(clef, text):
    # Vérifie si ligne n'est pas vide
    if text.strip() != 0:
        positionClef = text.find(clef)
        if verifyEntryIsWord(clef, text, positionClef):
            return(positionClef)
    return(-1)


def output(output_file, clef, pos, CUI):
    op = CUI + '|' + clef + '|' + str(pos)
    output_file.write(op + '\n')


def findEntries(thesaurus, oPath):
    outFilePath = 'mailtest.txt'
    with open(outFilePath,'w', encoding='utf-8') as ofile:
        subject = 'Nothign'
        temp = open('paper.txt','r',encoding='utf-8')
        body = ''
        for line in temp:
            body+=line
        for line in thesaurus:
            if line.strip() != "":
                clef = line.split('|')[0]
                CUI = line.split('|')[1].strip('\n')
                subject_pos = findEntryInText(clef, body)
                if (subject_pos != -1):
                    output(ofile, clef, subject_pos, CUI)


findEntries(thesaurus,'test.txt')

