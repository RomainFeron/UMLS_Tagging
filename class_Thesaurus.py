#!/usr/bin/env python
# -*- coding: utf-8 -*-

class thesaurus(object):

    def __init__(self, f):

        self.data = open(f, 'r', encoding='utf-8').readlines()
        self.length = len(self.data)

    def request(self, r):
        start = 0
        stop = self.length
        found = False
        while not found and start != stop:
            l = round((stop + start)/2)
            print(str(l) + '  ' + str(start) + '  ' + str(stop))
            print(self.data[l].split('|')[0] + '  ' + self.data[l+1].split('|')[0])
            if r < self.data[l].split('|')[0]:
                stop = l
            elif r > self.data[l].split('|')[0]:
                start = l
            else:
                found = True
                return(self.data[l].split('|')[2])
