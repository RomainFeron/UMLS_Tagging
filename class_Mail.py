#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import email.header
from langdetect import detect
# import os

"""La classe Mail est dédiée au stockage des informations contenue
 dans chaque email.
  Elle contient les attributs suivants: sujet (subject),
  envoyeur (sender), date (date), et contenu (body)."""


class Mail(object):

    # Crée un objet Mail à partir d'un fichier f

    def __init__(self, f):
        self.subject = ''  # Sujet de l'email
        self.sender = ''  # Envoyeur de l'email
        self.date = ''  # Date de l'email
        self.body = ''  # Contenu de l'email
        self.lang = 'fr'  # Langage de l'email (français par défaut)
        with open(f, encoding="utf-8") as mail:
            bodyFound = False
            for line in mail:
                # Récupère toutes les lignes faisant partie du contenu
                # de l'email
                if bodyFound:
                    self.body += line
                # Récupère la ligne contenant le sujet et formate le resultat
                # (enlève les tags au début de la ligne, enlève le \n à la fin
                # de la ligne) et indique que le contenu commence
                if line.startswith('Subject: '):
                    tempSubject = line
                    # Enleve tous les tags de l'email a partir de la balise ']'
                    while tempSubject.find(']') != -1:
                        tempSubject = tempSubject[
                            tempSubject.find(']') + 1:]
                    tempSubject = tempSubject[1:len(tempSubject) - 1]
                    tempSubject = email.header.decode_header(tempSubject)
                    for s, e in tempSubject:
                        if e is not None:
                            self.subject += s.decode(e)
                        else:
                            if s[0:1] != '=?':
                                self.subject += str(s)
                            else:
                                temp = s + '='
                                temp2 = email.header.decode_header(temp)
                                self.subject += temp2[0].decode(temp2[1])
                    bodyFound = True
                # Récupère la ligne contenant l'envoyeur et formate le resultat
                # (récupère seulement l'adresse mail contenue entre les '<>')
                if line.startswith('From: '):
                    self.sender = line[line.find('<') + 1:len(line) - 2]
                # Récupère la ligne contenant la date et formate le résultat en
                # un objet datetime
                if line.startswith('Date: ') and not bodyFound:
                    s = line[6:].replace(" ", "")
                    if s.find('+') != -1:
                        s = s[:s.find('+') + 5]
                    else:
                        s = s[:s.find('-') + 5]
                    s = s.replace(",", "")
                    s = s.replace(":", "")
                    self.date = datetime.datetime.strptime(
                        s, "%a%d%b%Y%H%M%S%z")
        # Trouve le langage de l'email avec la lib langdetect
        if len(self.body) > 10:
            self.lang = detect(self.body)

# Exemples d'utilisations de la classe
# testMail = Mail('Documents/bioinfo_2014-04/1.recoded')
# print('Subject: ', testMail.subject)
# print('From: ', testMail.sender)
# print('Date: ', testMail.date)
# print('Body:', testMail.body)
# print('Language:', testMail.lang)

# Juste un test pour voir si tous les fichiers mails pouvaient bien
# être ouverts et stockés dans une liste (prend quasiment pas de mémoire)
# listMails = []
# for root, directories, filenames in os.walk('Documents'):
#     for f in filenames:
#         if 'recoded' in f:
#             # print(os.path.join(root,f))
#             listMails.append(Mail(os.path.join(root, f)))
