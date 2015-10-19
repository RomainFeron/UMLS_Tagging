#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('Documents/FormattedThesaurus.RRF', 'r', encoding='utf-8')

thesaurus = f.readlines()

def makeRequest(request):
    found = False
    i=0
    while not found and i<len(thesaurus):
        if request == thesaurus[i].split('|')[0]:
            found = True
        i+=1
    if found:
        print(thesaurus[i-1])
    else:
        print("not found")

makeRequest('gene')
makeRequest('genetics')
makeRequest('agglomérats')

