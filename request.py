#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_Thesaurus import thesaurus
from class_Mail import Mail

thesaurus = thesaurus('ressources/FormattedThesaurus.RRF')

mail = Mail('Documents/bioinfo_2014-04/10.recoded')
print(mail.body)

text = 'The cell proteins are coded by a gene which has a certain function: Conorhinopsylla'

print('Thesaurus Loaded')


def request(thesaurus, text):
    res = []
    for line in thesaurus.data:
        concept = line.split('|')[0]
        pos = text.find(concept)
        if pos != -1:
            res.append([concept, line.split('|')[2][:-1], pos])
    return res

test = request(thesaurus, mail.body)
print(test)
