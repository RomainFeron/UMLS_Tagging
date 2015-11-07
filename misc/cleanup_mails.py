#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

mPath = 'ressources/mails'
for root, dirs, files in os.walk(mPath, topdown=False):
    for name in files:
        if '.recoded' not in name:
            print(os.path.join(root, name))
            os.remove(os.path.join(root, name))
