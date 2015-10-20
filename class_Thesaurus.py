#!/usr/bin/env python
# -*- coding: utf-8 -*-


class thesaurus(object):

    def __init__(self, f):

        rawFile = open(f, 'r', encoding='utf-8')
        self.data = rawFile.readlines()
        self.length = len(self.data)
        rawFile.close()
