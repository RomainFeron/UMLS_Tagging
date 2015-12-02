#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys

#debug
path1 = 'liste1.txt'
path2 = 'liste2.txt'

#path1 = sys.argv[1]
#path2 = sys.argv[2]

#file handlers
fh_ref = open(path1,'r',encoding='utf-8')
fh_out = open(path2,'r',encoding='utf-8')

#lists from reference|tagged inverted file
dic_ref = {}
dic_out = {}


def make_dic(dic, file):
    """
    create dictionnaries from 
    reference inverted cui file  and 
    output processed inverted cui file
    """
    for line in file:
        decoup = line.split('|')
        cui = decoup[0]
        list_fichier = decoup[1].split(',')
        for fichier in list_fichier:
            if cui in dic.keys():
                dic[cui].append(fichier)
            else:
                dic[cui] = [fichier]

def number_elements(dic):
    """
    return count of elements in a dictionnary
    """
    nb = 0
    for key in dic:
        for value in dic[key]:
          nb+=1
    return nb



def nb_match_two_dic(dic_ref, dic_tst):
    """
    return # match of dic_tst in dic_ref 
    """
    nb = 0
    for key in dic_tst:
        for value in dic_tst[key]:
            if value in dic_ref[key]:
                nb+=1
    return nb

                


print("dice ref")
make_dic(dic_ref, fh_ref)
print(dic_ref)

print("dic out")
make_dic(dic_out, fh_out)
print(dic_out)




relevant_elements = nb_match_two_dic(dic_ref, dic_out)
retrieved_elements = number_elements(dic_out)

print(relevant_elements)
print(retrieved_elements)


#precision
#precision = (retrieved_elements + retrieved_elements) / retrieved_elements
#recall :
#recal = (retrieved_elements + retrieved_elements) / relevant_elements

