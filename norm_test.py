# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:06:45 2023

@author: komij
"""

import os
import pandas as pd
from scipy import stats

os.chdir(r'C:\Users\komij\OneDrive\Desktop\CurrentWork\irritability')

df_All = pd.read_csv("allData.csv", usecols = ['ia1','ia2','ia3','ia4','ia5','ia6','ia7','ia8','ia9', 'ir1','ir2','ir3','ir4','ir5','h1','h2','h3','h4','h5','h6','im1','im2','im3', 'hyim_label'])
data_t = df_All.to_numpy()
res = stats.normaltest(data_t)
print(res)