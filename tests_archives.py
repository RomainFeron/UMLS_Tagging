# -*- coding: utf-8 -*-
import os
from langdetect import detect
import email.header

#Basic loop on all documents checking if language worked
with open('Documents/bioinfo_2014-02/1.recoded', encoding="utf-8") as mail:
    for root, directories, filenames in os.walk('Documents'):
        for f in filenames:
            if 'recoded' in f:
                testMail ''= Mail(os.path.join(root,f))
                print(os.path.join(root,f))
                if testMail.lang != 'fr':
                    print(root+'/'+f+'/'+testMail.lang)

#Basic test on subject parsing from only one file
f='Documents/bioinfo_2014-04/1.recoded'
subject=''
with open(f, encoding="utf-8") as mail:
    for line in mail:
        if line.startswith('Subject: '):
            tempSubject = line
            # Enleve tous les tags de l'email a partir de la balise ']'
            while tempSubject.find(']') != -1:
                tempSubject = tempSubject[
                    tempSubject.find(']') + 1:]
            tempSubject = tempSubject[1:len(tempSubject) - 1]
            tempSubject = email.header.decode_header(tempSubject)
            print(tempSubject)
            for s, e in tempSubject:
                if e != None:
                    print(e)
                    subject += s.decode('utf - 8')
                else:
                    subject += s
            print(subject)

#Test on subject parsing for all the files
for root, directories, filenames in os.walk('Documents'):
    for f in filenames:
        if 'recoded' in f:
            print(os.path.join(root,f))
            subject=''
            with open(os.path.join(root,f), encoding="utf-8") as mail:
                for line in mail:
                    if line.startswith('Subject: '):
                        tempSubject = line
                        # Enleve tous les tags de l'email a partir de la balise ']'
                        while tempSubject.find(']') != -1:
                            tempSubject = tempSubject[
                                tempSubject.find(']') + 1:]
                        tempSubject = tempSubject[1:len(tempSubject) - 1]
                        tempSubject = email.header.decode_header(tempSubject)
                        for s, e in tempSubject:
                            if e != None:
                                subject += s.decode(e)
                            else:
                                if s[0:1]!='=?':
                                    subject += str(s)
                                else:
                                    temp=s+'='
                                    temp2=email.header.decode_header(temp)
                                    subject+= temp2[0].decode(temp2[1])
                        print(subject)

#email decoder test
x="CDI =?WINDOWS-1252?Q? ?= Chef de Projet en analyse de =?WINDOWS-1252?Q?données?= =?WINDOWS-1252?Q?génomiques?"
y=email.header.decode_header(x)
print(y)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
import linecache

l = []
rawThesaurus = open('Documents/MRCONSO_2011AA.RRF', encoding='utf-8')

# Benchmark:
# t = 8.7s
# RAM négligeable
for i, line in enumerate(rawThesaurus):
    if i in range(500000, 600000):
        l.append(line)
print(l[50000])

# Benchmark:
# t = 5.7s
# RAM : 1.7 GB
for i in range(500000, 600000):
    l.append(linecache.getline('Documents/MRCONSO_2011AA.RRF', i))
print(l[50000])

# Benchmark:
# t = 5.5s pour 500000 - 600000
# RAM : 1.6 GB
crazy = rawThesaurus.readlines()
for i in range(500000, 600000):
    l.append(crazy[i])
print(l[50000])


l = [['genet','ENG','C0325074'],['gene','ENG','C0017337'], ['geng-tang','ENG','C0670194']]

def getKey(item):
    return item[0]

fT = sorted(l,key = getKey)
print(fT)
