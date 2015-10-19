#!/usr/bin/env python
# -*- coding: utf-8 -*-
import linecache

l = []
rawThesaurus = open('Documents/MRCONSO_2011AA.RRF', encoding='utf-8')

# Benchmark:
# t = 8.7s
# RAM négligeable
for i, line in enumerate(rawThesaurus):
    if i in range(500000, 600000):
        l.append(line)
print(l[50000])

# Benchmark:
# t = 5.7s
# RAM : 1.7 GB
for i in range(500000, 600000):
    l.append(linecache.getline('Documents/MRCONSO_2011AA.RRF', i))
print(l[50000])

# Benchmark:
# t = 5.5s pour 500000 - 600000
# RAM : 1.6 GB
crazy = rawThesaurus.readlines()
for i in range(500000, 600000):
    l.append(crazy[i])
print(l[50000])
