#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_Mail import Mail

thesaurus = open('ressources/FormattedThesaurus.RRF','r',encoding = 'utf-8')
#data = thesaurus.readlines()

mail = Mail('ressources/mails/bioinfo_2014-04/10.recoded')
text = 'The cell proteins are coded by a gene which has a certain function: Conorhinopsylla'

print('Thesaurus Loaded')

def request(data, text):
    res = []
    for line in data:
        concept = line.split('|')[0]
        pos = text.find(concept)
        
        if pos != -1:
            res.append([concept, line.split('|')[1][:-1], pos])
    return res

test = request(thesaurus, mail.body)
print(test)
