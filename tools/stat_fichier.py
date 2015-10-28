#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys

""" File to be tested passed as argument """


nb_ligne = 0

with open(sys.argv[1],'r',encoding='utf-8') as fh:
    start = time.time()
    for line in fh:
        nb_ligne += 1
    end = time.time()

temps = end - start
        
print('Fichier: ' + sys.argv[1])
print('Nombre de lignes dans le fichier: ' + str(nb_ligne))
print('Temps mis pour le parcours: ' + str(temps))
