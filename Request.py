#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Verifie que l'entrée du thésaurus est bien un mot en comparant les
# caractères à gauche et à droite du match à une liste de termes OK
def verifyEntryIsWord(clef, text, pos):
    okChar = [' ', '.', ',', ';', ':', '-']
    if clef in text:
        if pos - 1 > 0 and pos + len(clef) + 1 <= len(text):
            if text[pos - 1] == " " and text[pos + len(clef)] in okChar:
                return(True)
    return(False)


# Renvoie la position d'un match de l'entrée du thésaurus (-1 si pas de match)
def findEntryInText(clef, text):
    # Vérifie si la ligne de l'email n'est pas vide
    if text.strip() != "":
        positionClef = text.find(clef)
        #
        if verifyEntryIsWord(clef, text, positionClef):
            return(positionClef)
    return(-1)


# Ecrit le résultat dans le fichier output
def output(output_file, clef, pos, CUI, mail, mailPart):
    op = CUI + '|' + clef + '|' + str(pos) + '|' + mailPart + '|' + mail
    output_file.write(op + '\n')


# Cherche les entrées du thésaurus dans un mail
def findEntries(thesaurus, mail, oPath):
    # Output file dans dossier oPath: nom de l'email .txt
    outFilePath = oPath + '/' + mail.title + '.txt'
    with open(outFilePath, 'w', encoding='utf-8') as ofile:
        subject = mail.subject
        body = mail.body
        for line in thesaurus:
            # Vérifie que la ligne du thésaurus n'est pas vide
            if line.strip() != "":
                clef = line.split('|')[0]
                CUI = line.split('|')[1].strip('\n')
                # Trouve position du match dans l'email (-1 si non match)
                subject_pos = findEntryInText(clef, subject)  # Dans le sujet
                if (subject_pos != -1):
                    output(ofile, clef, subject_pos, CUI, mail.title, 'S')
                body_pos = findEntryInText(clef, body)  # Dans le body
                if (body_pos != -1):
                    output(ofile, clef, body_pos, CUI, mail.title, 'B')
