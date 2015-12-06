#!/usr/bin/env python
# -*- coding: utf-8 -*-


l = []

#file_path = "./extrait.txt"
file_path = './MRCONSO_2011AA.RRF'

# numero absolu des colonnes (commence a 1!); selon ordre voulu
selected_col= [15, 2, 1]
compteur = 0
ma_liste = []

languagesSel = ['FRE','ENG']

def afficheListe (liste):
    for element in liste:
        print(element)

# Selection des donnees pertinentes et rearrangement des colonnes langue / string / CUI
with open(file_path, 'r', encoding='utf-8') as fichier:
    for line in fichier:
        l = line.split('|')
        #print(l)
        if (l[2-1] in languagesSel):
        #if (l[2-1] == 'FRE'):
            res = ''
            for n_col in selected_col:
                res = res + str(l[n_col - 1]) + '|'
            # print(res)
            ma_liste.append(res)
            compteur += 1



# print(ma_liste)
ma_liste.sort()

afficheListe(ma_liste)


"""

name_file = 'MRCONSO_2011AA.RRF'

"""
"""
file_path2 = 'theausaurus_mod.txt'
with open(file_path2, 'w', encoding='utf-8') as fichier2:
    fichier2.write('Hallo\nCommo esta?')
    #fichier2.write(str(afficheListe(ma_liste)))
fichier2.close()
"""
