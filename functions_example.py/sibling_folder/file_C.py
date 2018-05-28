# -*- coding: utf-8 -*-
"""
Created on Wed May 23 09:36:56 2018

@author: tommy_mizuki
"""

def subtract_and_increment(a, b):
    """"
    Return a minus b, plus 1
    """
    c = a - b + 1
    return c

import sys
print(sys.path, end="\n\n")

# Add a directory
sys.path.append('../')
print(sys.path, end="\n\n")

# Remove a directory
sys.path.remove('../')
print(sys.path)
sys.path.append('../../another_example')