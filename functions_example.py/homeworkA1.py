# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 16:53:38 2018

@author: tommy_mizuki
"""
import numpy as np
import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
#Import the data
data = pd.read_csv(url, sep = '|')
#Check if I could import the data

sort_list = [];
##while data.shape[0] > 0:
#    name = data["occupation"][0]
#    print(name)
#    A = data.index[(data.occupation == name)] 
##    print(A)
#    data.drop(index = A.tolist(), inplace = True)
##print(data.shape[0])
#    sort_list.append(A)
    
    
#for raw in data["occupation"]:
#    #A = data.index[(data.occupation == name)] 
#    #if data.occupation == raw:
#    A1 = data[data['occupation'] == raw]
#    print(len(A1['occupation']))
#    #data  = data.drop(data['occupation']==raw)
#    data = data[data.occupation != raw]
#    print(data.head())
    
    
A1 = data.drop_duplicates("occupation")
print(A1)
new_list = []
for raw in A1["occupation"]:
    A = len(data[data['occupation'] == raw]['occupation'])
    print(A)
    new_list.append(A)
print(new_list)