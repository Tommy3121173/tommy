# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:58:03 2018

@author: tommy_mizuki
"""

import sys
print(sys.path, end="\n\n")

# Add a directory
sys.path.append('../')
print(sys.path, end="\n\n")

# Remove a directory
sys.path.remove('../')
print(sys.path)

sys.path.append('../functions_example)