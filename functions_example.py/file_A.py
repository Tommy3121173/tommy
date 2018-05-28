# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:40:58 2018

@author: tommy_mizuki
"""

import file_B

file_B.print_a_number(4)

file_B.type_interrogate('hello')
  
from file_B import *

print_a_number(4)

type_interrogate('hello')

from sibling_folder.file_C import *

print(subtract_and_increment(8, 10))


