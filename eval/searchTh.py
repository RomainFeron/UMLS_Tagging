import re
import sys

"""Recherche d'une chaine de caractère dans le FormatedTh
exple utilisation: python3 searchTh.py ' analyses? * réseaux? '
"""


pathTh= '../ressources/FormattedThesaurus.RRF'
#pathTh = './fichier_tst.txt'

fh = open(pathTh,'r',encoding='utf-8')

query = sys.argv[1]
res=[]
#res = re.IGNORECASE(query, pathTh)
for line in fh:
#    re.IGNORECASE
    if (re.search(query, line, re.IGNORECASE)):
        print(line)

#print(res)
