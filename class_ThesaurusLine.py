#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


class MetaThesaurusLine(object):

    def __init__(self, l):
        temp = l.split('|')
        self.cui = temp[0]
        self.lat = temp[1]
        self.ts = temp[2]
        self.lui = temp[3]
        self.stt = temp[4]
        self.sui = temp[5]
        self.ispref = temp[6]
        self.aui = temp[7]
        self.saui = temp[8]
        self.scui = temp[9]
        self.sdui = temp[10]
        self.sab = temp[11]
        self.tty = temp[12]
        self.code = temp[13]
        self.string = temp[14]
        self.srl = temp[15]
        self.suppress = temp[16]
        self.cvf = temp[17]


# l = "C0000005|ENG|P|L0000005|PF|S0007492|Y|A7755565||M0019694|D012711|MSH|PEN|D012711|(131)I-Macroaggregated Albumin|0|N||"
# testLine = MetaThesaurusLine(l)
# print(testLine.cui)w
