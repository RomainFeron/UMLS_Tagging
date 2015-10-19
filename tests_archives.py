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
