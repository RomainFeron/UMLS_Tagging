#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def findEntrie(thesaurus, email, output):
    TH = open(thesaurus,'r',encoding = 'utf-8')
    print ('reading thesaurus...')
    out = open (output, 'w', encoding = 'utf-8')
    sp= ' '
    dico_clef = {}
    for line in TH:
        # Vérifie si line n'est pas vide
        if line.strip()!="":
        # line = line[:-1]
            clef = line.split('|')[0]
            mail = open (email, 'r',encoding = 'utf-8' )
            #Comteur du nombre de ligne dans mon mail
            # nbreligne=1
            # rep=0
            dict_ligne = {} # stockage de mes lignes dans le mail
            for ligne in mail:
                mypos = ligne.find(clef)
                if ligne.strip()!=0:
                    if clef in ligne and ligne[mypos-1] == sp :
                        # print (clef)
                        if True:
                            listemot=ligne.split(clef)
                            bef = listemot[0].split()
                            aft = listemot[1].split()
                            len_b = len(bef)
                            len_a = len(aft)
                            wb = bef[len_b -1]
                            wa = aft[len_a -1]
                            print ('la clef --', clef)
                            print ('mot avant = ', wb)
                            print ('la position est', mypos )
                            print ('mot après = ', wa)
                            print (' line in Thesaurus = ', line)
                            nbr=len(ligne.split(clef))-1
                            out.write (' Entrée trouvée dans le mail --->' +'\t'+ clef +'\n'+ ' Position = ' + str(mypos) + 'th character' +'\n'+ ' Line in Thesaurus = ' + line + 'Context dans le mail : ' + '\t' +  wb +sp+clef+sp+  wa + '\n'+'-------------------' + '\n')

    out.close()
email = 'ressources/mails/bioinfo_2014-01/58.recoded'
# 'bodymail_test.txt'
thesaurus = 'ressources/FormattedThesaurus.RRF'
output = 'sortie.txt'
test = findEntrie(thesaurus, email, output)
