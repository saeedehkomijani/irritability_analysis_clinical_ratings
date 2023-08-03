# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:38:35 2023

@author: komij
"""

import math
import os
import pandas as pd

os.chdir(r'C:\Users\komij\OneDrive\Desktop\CurrentWork\irritability')

#Dataset1: subjects with second year of data
#Dataset2: subjects without second year of data

df_A = pd.read_csv("dataset1.csv", usecols = ['ia1','ia2','ia3','ia4','ia5','ia6','ia7','ia8','ia9', 'ir1','ir2','ir3','ir4','ir5','h1','h2','h3','h4','h5','h6','im1','im2','im3'])
df_B = pd.read_csv("dataset2.csv", usecols = ['ia1','ia2','ia3','ia4','ia5','ia6','ia7','ia8','ia9', 'ir1','ir2','ir3','ir4','ir5','h1','h2','h3','h4','h5','h6','im1','im2','im3'])
df_labels = pd.read_csv("dataset1.csv", usecols = ['hyim_T2'])

dt_A = df_A.to_numpy()
dt_B = df_B.to_numpy()
dt_labels = df_labels.to_numpy()

print(dt_A[0])
print(dt_B[0])


for j in range(0,24):
    min = 10000
    for i in range(0,31):
        eDistance = math.dist(dt_A[i], dt_B[j])
        if(eDistance < min):
            min_index = i
            min = eDistance
            
    print(min_index, dt_labels[min_index], min)

