# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 16:16:54 2018

@author: tommy_mizuki
"""
import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
#Import the data
data = pd.read_csv(url, sep = '|')
#Check if I could import the data
print(data)

A = data.index[(data.occupation == 'other')] 
B = data.index[(data.occupation == 'retired')]

data.drop(index = A.tolist(),inplace = True)
data.drop(index = B.tolist(),inplace =True)
print(data)


import matplotlib.pyplot as plt
import numpy as np
sort_list = [];
A1 = data.drop_duplicates("occupation")
print(A1)
new_list = []
for raw in A1["occupation"]:
    A = len(data[data['occupation'] == raw]['occupation'])
    new_list.append(A)
print(new_list)

new_array = np.array(new_list)
#print(new_list1)
B = list(A1['occupation'])
#print(B)
B1 = np.array([B,new_array])
#print(B1)
#print(np.argsort(new_list1)[::-1])
B2 = B1[:, np.argsort(new_array)[::-1]]
print(B2)
C1 = B2[:,:10]
print(C1)
C2 = B2[:,10:]
print(C2)
D1 = list(map(int,C2[1]))
D2 = sum(D1)
print(type(D2))
print(D2)
P = list(C1[0])
P.append('other')
print(P)
Q = list(map(int,C1[1]))
Q.append(D2)
print(Q)

# Create an array with the position of each bar along the x-axis
x_pos = np.arange(len(P))
# Produce bar plot
plt.bar(x_pos, Q);

# Replace the x ticks with the year group name
# Rotate labels 30 degrees
plt.xticks(x_pos, P, rotation=90);
# Add axis labels 
#plt.xlabel('occupation');
#plt.ylabel('number of people');