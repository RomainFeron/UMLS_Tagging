import os


""" Petit test en cours : les mails sont encodés dans des formats différents (certains en UTF-8 et certains ont en plus d'autres caractères dans d'autres formats... Cette boucle ouvre tous les emails les uns après les autres, pour voir là où il y a des erreurs)
  Solution possible: ouvrir le fichier en bytes (mode binaire) ? """

k=0

for root, directories, filenames in os.walk('Documents'):
  for f in filenames:
    if 'recoded' in f:
      print(f)
      with open(os.path.join(root,f), encoding="utf-8") as mail:
        for line in mail:
          #print(line)
          k+=1

