#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from class_Mail import Mail


def verifyEntryIsWord(clef, text, pos):
    okChar = [' ', '.', ',', ';', ':']
    if clef in text:
        if pos - 1 > 0 and pos + len(clef) + 1 <= len(text):
            if text[pos - 1] == " " and text[pos + len(clef)] in okChar:
                return(True)
    return(False)


def findEntryInText(clef, text):
    # Vérifie si line n'est pas vide
    if text.strip() != 0:
        positionClef = text.find(clef)
        if verifyEntryIsWord(clef, text, positionClef):
            return(positionClef)
    return(-1)


def output(output_file, clef, pos, CUI, mail, mailPart):
    op = CUI + '|' + clef + '|' + str(pos) + '|' + mailPart + '|' + mail
    output_file.write(op + '\n')


def findEntries(thesaurus, mail, oPath):
    outFilePath = oPath + '/' + mail.title + '.txt'
    with open(outFilePath,'w', encoding='utf-8') as ofile:
        subject = mail.subject
        body = mail.body
        for line in thesaurus:
            if line.strip() != "":
                clef = line.split('|')[0]
                CUI = line.split('|')[1].strip('\n')
                subject_pos = findEntryInText(clef, subject)
                if (subject_pos != -1):
                    output(ofile, clef, subject_pos, CUI, mail.title, 'S')
                body_pos = findEntryInText(clef, body)
                if (body_pos != -1):
                    output(ofile, clef, body_pos, CUI, mail.title, 'B')


# email = Mail('ressources/mails/bioinfo_2014-01/58.recoded')
# # 'bodymail_test.txt'
# f = open('ressources/FormattedThesaurus.RRF', encoding='utf-8')
# thesaurus = list(f)
# f.close()
# ofilePath = 'sortie.txt'
# ofile = open(ofilePath, 'w', encoding='utf-8')
# test = findEntries(thesaurus, email, ofile)
