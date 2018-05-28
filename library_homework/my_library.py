# -*- coding: utf-8 -*-
"""
Created on Wed May 23 16:54:52 2018

@author: tommy_mizuki
"""

def my_func(x,y):
    import numpy as np
    element0 = np.cos(x) + 10*y
    element1 = np.sin(x) - 20*y
    A = [element0,element1]
    print(A)
