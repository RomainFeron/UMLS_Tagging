
# -*- coding: utf-8 -*-
import codecs

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def delete_stopW (mail_in= 'bodymail_test.txt'): #stop_wlist= 'French.txt')
    # sw = open ('French.txt', 'r')

    # with open ('stop_wlist') as sw:
    # with open ('bodymail_test.txt', ) as bodymail:
    bodymail = codecs.open ('bodymail_test.txt', 'r', "utf-8")
    sw = stopwords.words("french")
    # with open ('mail_out') as mail:
    mail_f = ''
    for word in bodymail:
        mail_f = mail_f+word
        word_list = word_tokenize(mail_f)
        for w in word_list:
            if w not in sw:
                print 'mot important :', w
            # # print w
            # tag = nltk.pos_tag(word_list)
            # if
            # word_list=[]
            # print word
            # for w in mail_f.split():
            #     # print w
            #     if w not in sw:
            #         word_list.append(w)
            #         print (word_list)
    return
    bodymail.close()


# stop_wlist = 'French.txt'
# mail_in = 'bodymail_test.txt'
delete_stopW ('bodymail_test.txt')
