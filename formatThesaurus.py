#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_ThesaurusLine import MetaThesaurusLine

l = []
with open('extract.txt', 'r', encoding='utf-8') as fichier:

    crazy = rawThesaurus.readlines()
    test = MetaThesaurusLine(crazy[152])
print(crazy[152])
print('CUI : ' + test.cui)
print('LANGUAGE : ' + test.lat)
print('STRING : ' + test.string)
