# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:06:45 2023

@author: komij
"""

import os
import pandas as pd
from scipy import stats

os.chdir(r'C:\Users\komij\OneDrive\Desktop\CurrentWork\irritability')

df_A = pd.read_csv("dataset1.csv", usecols = ['IQ', 'age','ia1','ia2','ia3','ia4','ia5','ia6','ia7','ia8','ia9', 'ir1','ir2','ir3','ir4','ir5','h1','h2','h3','h4','h5','h6','im1','im2','im3'])
df_B = pd.read_csv("dataset2.csv", usecols = ['IQ', 'age','ia1','ia2','ia3','ia4','ia5','ia6','ia7','ia8','ia9', 'ir1','ir2','ir3','ir4','ir5','h1','h2','h3','h4','h5','h6','im1','im2','im3'])
df_labels = pd.read_csv("dataset1.csv", usecols = ['hyim_T2'])

dt_A = df_A.to_numpy()
dt_B = df_B.to_numpy()

dt_labels = df_labels.to_numpy()

#print(df_A.mean(), df_B.mean())
feature_names = ['ia1','ia2','ia3','ia4','ia5','ia6','ia7','ia8','ia9', 'ir1','ir2','ir3','ir4','ir5','h1','h2','h3','h4','h5','h6','im1','im2','im3']

#for i in feature_names:
    #print(stats.ttest_ind(df_A[i], df_B[i],equal_var=False))


df_All = pd.read_csv("allData.csv", usecols = ['ia1','ia2','ia3','ia4','ia5','ia6','ia7','ia8','ia9', 'ir1','ir2','ir3','ir4','ir5','h1','h2','h3','h4','h5','h6','im1','im2','im3', 'hyim_label'])
data_t = df_All.to_numpy()
res = stats.normaltest(data_t)
print(res)