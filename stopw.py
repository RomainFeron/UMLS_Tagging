
# -*- coding: utf-8 -*-

import codecs
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

'''Cette fonction prend comme entrée un bodymail, le tokenise, enlève les stopwords et renvoie une liste de mots importants stocké dans une liste'''

def delete_stopW (mail_in= 'bodymail_test.txt'): # Argument à changer en fonction de votre mail à tester

    bodymail = codecs.open ('bodymail_test.txt', 'r', "utf-8")
    sw = stopwords.words("french")
    mail_f = ''
    for word in bodymail:
        mail_f = mail_f + word
        # pont = ['.',',',';','(',')']
        WD = word_tokenize(mail_f)
        My_Word_list = ''
        for w in WD:
            if w not in sw:
                My_Word_list = My_Word_list+w
                # print 'mot important :', w

    return
    bodymail.close()

delete_stopW ('bodymail_test.txt')
