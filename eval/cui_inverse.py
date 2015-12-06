#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

#path to target files
path_ref = './cp_docs'
path_process = '../output'
#outputs names
output_file_ref = 'list_cui_ref.txt'
output_file_process = 'list_cui_process.txt'
#filetypes
filetype_ref = 'eval'
filetype_process = 'txt'

def list_files (path, filetype):
    """
    return list path of determined filetype
    """
    list = []
    for root, directories, filenames in os.walk(path):
        for f in filenames:
            if filetype in f:
                list.append(os.path.join(root,f))
    print("#files found: " + str(len(list)))
    return list

def extract_cui (list_file):
    list_cui = {}
    for file in list_file:
        fh = open(file,'r',encoding='utf-8')
        for line in fh:
            if line in list_cui:
                list_cui[line].append(file)
            else:
                list_cui[line] = [file]
    return list_cui

def write_file_ref(list_cui, output_file):
    """
    writes a clean file of ref cui list
    """
    output = open(output_file, 'w', encoding='utf-8')
    for key in list_cui:
        cle = str(key.strip('\n'))
        val = str(list_cui[key])
        res = ''
        res = res + cle +'|'+ val +'\n'
        res = res.strip("[")
        res = res.strip("]")
        res = res.strip("'")
        res = res.replace('[\'./cp_docs/', '')
        res = res.replace('.recoded.eval\']','')
        res = res.replace('/','_')
        
        #print(res)
        output.write(res)
    output.close()


def write_file_process(list_cui, output_file):
    """
    writes a cleaned file a process cui list
    """
    output = open(output_file, 'w', encoding='utf-8')
    for line in list_cui:
        #line = str(line.strip('\n'))
        line = line.strip('\n')
        tab_string = line.split('|')
        #print(len(tab_string))
        cui = tab_string[0]
        val = tab_string[4]
        res = ''
        res = res + cui + '|' + val +'\n'
        #print(res)
        output.write(res)
    output.close()



#list target files
print('\nListing reference files')
list_file_ref = list_files(path_ref,filetype_ref)
#print('Number of files: ' + str(len(list_file_ref)))
#print(list_file_ref)

print('\nListing processed files')
list_file_process = list_files(path_process,filetype_process)
#print('Number of files: ' + str(len(list_file_process)))
#print(list_file_process)


#inverted list of cui references 
list_cui_ref = {}
list_cui_ref = extract_cui(list_file_ref)
#print(list_cui_ref)


write_file_ref(list_cui_ref, output_file_ref)
print('\nInverted ref CUI file generated: ', output_file_ref)


#inverted list of cui process
list_cui_process = {}
list_cui_process = extract_cui(list_file_process)
#print(list_cui_process)

write_file_process(list_cui_process, output_file_process)
print('\nInverted processed CUI file generated: ', output_file_process)

print('\n\nNext step : compute recall and precision with comp_cui')



nb_unik_cui_ref = 0
nb_cui_ref = 0

for key in list_cui_ref:
    nb_unik_cui_ref +=1
    for value in list_cui_ref[key]:
        nb_cui_ref +=1

print("Number of unique CUI in ref: ", nb_unik_cui_ref)
print("Number of CUI in ref: ", nb_cui_ref)



print(len(set(list_cui_process)))



"""
Marked processed files 
"""



#print(type(list_file_ref))

list_marked_files = []
for e in list_file_ref:
    tmp = e.replace('./cp_docs','../output')
    tmp = tmp.replace('.recoded.eval','')
    tmp = tmp.replace('~','')
    tab = tmp.split('/')
#    str = tab[0] + '/' + tab[1] + '/' + tab[2] + '_' tab[3]
    str = tab[0] + '/' +tab[1] + '/' + tab[2] + '_' + tab[3] + '.txt'
    list_marked_files.append(str)

output_file_process_marked = 'list_cui_process_marked.txt'

list_cui_process_marked = extract_cui(list_marked_files)

write_file_process(list_cui_process_marked, output_file_process_marked)


