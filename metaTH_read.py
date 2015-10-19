
# -*- coding: utf-8 -*-
import codecs
import os
# from stopw import *


def open_MT_file (Meta = 'MRCONSO_2011AA.RRF', mail_in= 'bodymail_test.txt'):
    # with (Meta) open as MTfile:
    bodymail = codecs.open ('bodymail_test.txt', 'r', "utf-8")
    MTfile = codecs.open ('MRCONSO_2011AA.RRF', 'r', "utf-8")
    # x= delete_stopW (mail_in= 'bodymail_test.txt')
    for line in MTfile:
        tag = line.split('|')
        text = ''
        for mot in bodymail:
            text = text+mot
            for word in text:
                print 'voici un mot:', word
                while True:
                    pass
                    if word in tag:
                        print line
                        return line

    return

    bodymail.close()
    MTfile.close()
open_MT_file()
