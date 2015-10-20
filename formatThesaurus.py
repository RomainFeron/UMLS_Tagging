#!/usr/bin/env python
# -*- coding: utf-8 -*-

rawThesaurus = open('Documents/MRCONSO_2011AA.RRF', 'r', encoding='utf-8')

languagesSelected = ['FRE', 'ENG']

""" Exemple de ligne:
C0000005|ENG|P|L0000005|PF|S0007492|Y|A7755565||M0019694|D012711|MSH|
PEN|D012711|(131)I-Macroaggregated Albumin|0|N||
"""

""" Pour cette ligne, explication:

    cui = C0000005 -> Unique identifier for concept
    lat = ENG -> Language of term
    ts = P -> Term status
    lui = L0000005 -> Unique identifier for term
    stt = PF -> String type
    sui = S0007492 -> Unique identifier for string
    ispref = Y -> Atom status preferred (Y/N)
    aui = A7755565 -> Unique identifier for atom
    saui = '' -> Source asserted atom identifier
    scui = M0019694 -> Source asserted concept identifier
    sdui = D012711 -> Source asserted descriptor identifier
    sab = MSH -> Abbreviated source name
    tty = PEN -> Abbreviation for term type in source vocabulary
    code = D012711 -> Most useful source asserted identifier
    string = (131)I-Macroaggregated Albumin -> String
    srl = 0 -> Source restriction level
    suppress = N -> Suppressible flag
    cvf = '' - Content View Flag

"""

formattedThesaurus = open('Documents/FormattedThesaurus.RRF', 'w', encoding='utf-8')


ft = []
for line in rawThesaurus:
    temp = line.split('|')
    if temp[1] in languagesSelected:
        l = temp[14] + "|" + temp[1] + "|" + temp[0] + ' \n '
        ft.append(l)

ft = set(ft)

for i in ft:
    formattedThesaurus.write(i)
