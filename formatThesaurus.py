#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_ThesaurusLine import MetaThesaurusLine

l = []
rawThesaurus = open('Documents/MRCONSO_2011AA.RRF', 'r', encoding='utf-8')
formattedThesaurus = open('Documents/Thesaurus.RRF', 'w', encoding='utf-8')
crazy = rawThesaurus.readlines()
test = MetaThesaurusLine(crazy[152])
print(crazy[152])
print('CUI : ' + test.cui)
print('LANGUAGE : ' + test.lat)
print('STRING : ' + test.string)
