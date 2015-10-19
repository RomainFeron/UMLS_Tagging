#!/usr/bin/env python
# -*- coding: utf-8 -*-

from class_Thesaurus import thesaurus

thesaurus = thesaurus('Documents/FormattedThesaurus2.RRF')

def makeRequest(request):
    found = False
    i=0
    while not found and i<thesaurus.length:
        if request == thesaurus.data[i].split('|')[0]:
            found = True
        i+=1
    if found:
        print(thesaurus.data[i-1])
        print(i)
    else:
        print("not found")

#makeRequest('gene')

print('genet'<'gene')
print(thesaurus.data[5251827])
print(thesaurus.data[5251828])
print(thesaurus.data[5251829])
print(thesaurus.data[5251830])

#print(thesaurus.request('gene'))


