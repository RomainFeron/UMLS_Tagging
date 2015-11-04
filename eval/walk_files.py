#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import random


"""listage ensemble des fichiers"""
listFile = []
for root, directories, filenames in os.walk('../ressources'):
    for f in filenames:
        if 'recoded' in f:
            listFile.append(os.path.join(root,f))
print("Nb fichiers: " + str(len(listFile)))

"""chemin des E-mails references"""
nb_extrait = 60 # nb d'email a extraire
sel = []
random.seed(3,version=2) # fixation seed
sel = random.sample(listFile,nb_extrait)
print(sel)



"""copie des E-mail selectionnes"""
for file in sel:
    path = "./cp_docs"
    # Construction du nom cible
    cpfich = os.path.split(file)
    dir = os.path.basename(cpfich[0])
    path = os.path.join(path,dir,cpfich[1])
    #sortie confirmation
    #print("source: " +file + "    dest: " +path + "   rep: " +os.path.dirname(path)) #complet avec path intermediaires
    print("   rep: " +os.path.dirname(path))

    if not os.path.isdir(os.path.dirname(path)):
        os.mkdir(os.path.dirname(path))
    shutil.copy(file, path)




    
