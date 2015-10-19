#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_Thesaurus import thesaurus
from class_Mail import Mail

thesaurus = thesaurus('Documents/FormattedThesaurus.RRF')

mail = Mail('Documents/bioinfo_2014-04/10.recoded')


def request(thesaurus, text):
    res = []
    i = 0
    for line in thesaurus.data:
        if(i % 1000 == 0):
            print(i)
        concept = line.split('|')[0]
        pos = text.find(concept)
        if pos != -1:
            res.append([concept, line.split('|')[2], pos])
        i += 1
    return res

test = request(thesaurus, mail.body)
