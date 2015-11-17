#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

''' Fontion Requête : Input = Thesaurus et bodymail, output = words, position in mail and the line in the Thesaurus'''
def findEntrie(thesaurus, email, output):
    TH = open(thesaurus,'r',encoding = 'utf-8')
    mail = open (email, 'r',encoding = 'utf-8' )
    text = ''
    for line in mail:
        text= text+line
    out = open (output, 'w', encoding = 'utf-8')
    myword = []
    sp= ' '
    for line in TH:
        line = line[:-1]
        clef = line.split('|')[0]
        if clef in text:
            x= len(clef)
            mypos = text.index(clef)
            if text[mypos-1] == sp:
                #Pour recuperer après l'entrée la plus longue
                myword.append(clef)
                p = myword.sort (key=len, reverse =True)
                c=False
                if x != -1:
                    w = clef.split(sp)[0]
                    c = myword.count(w)
                    if c >= 1:
                        print (c)

            out.write (' Word(s) in mail = ' + clef +'\n'+ ' Position = ' +  str(mypos) + 'th character' +'\n'+ ' Line in Thesaurus = ' + line +'\n')

    out.close()
email = 'bodymail.txt'
thesaurus = 'formattedThesaurus'
output = 'fichierDeSortie.txt'
test = findEntrie(thesaurus, email, output)
