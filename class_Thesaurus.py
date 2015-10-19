#!/usr/bin/env python
# -*- coding: utf-8 -*-


class thesaurus(object):

    def __init__(self, f):

        self.data = open(f, 'r', encoding='utf-8').readlines()
        self.length = len(self.data)
