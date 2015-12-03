#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


#path to target files
path_ref = './cp_docs'
path_process = '../output'
#outputs names
output_file_ref = 'list_cui_ref.txt'
output_file_process = 'list_cui_process.txt'


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
        line = str(line.strip('\n'))
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
list_file_ref = list_files(path_ref,'eval')
#print(list_file_ref)

print('\nListing processed files')
list_file_process = list_files(path_process,'txt')
#print(list_file_process)


#inverted list of cui references 
list_cui_ref = {}
list_cui_ref = extract_cui(list_file_ref)
# print(list_cui_ref)
write_file_ref(list_cui_ref, output_file_ref)
print('\nInverted ref CUI file generated: ', output_file_ref)

#inverted list of cui process
list_cui_process = {}
list_cui_process = extract_cui(list_file_process)

#print(list_cui_process)
write_file_process(list_cui_process, output_file_process)
print('\nInverted processed CUI file generated: ', output_file_process)

print('\n\nNext step : compute recall and precision with comp_cui')


"""
fh = open(path,'r',encoding='utf-8')
for line in fh:
    tab_string = line.split('|')
    cui = tab_string[0]
    file = tab_string[4]
    
    
    if line in list_cui:
        list_cui[line].append(file)
    else:
        list_cui[line] = [file]


print("Liste des CUIs et leurs sources")
print(list_cui)
"""
