# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 06:33:01 2020

@author: Amarnath
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('e:/anitha/marks.csv')

#print(df.head())

print(df.loc[-11])
#print(df.iloc[-12])

#print(df.iloc[-1])

subset=df.loc[2:2,['Roll No','Name of the Student']]

#print(subset)

#subset=df.iloc[2:2,['Roll No','Name of the Student']]

print(subset)


#subset=df.iloc[:,[2,4,-1]]

#print(subset)


#myrange = list(range(7))
#print(myrange)
#subset = df.iloc[:, myrange]

#print(subset)


#myaggre = df.groupby(['Batch','Sr No'])[['1','2']].mean()
#print(myaggre)

#myaggre = df.groupby(['Batch','Sr No'])[['1','2']].mean()
#print(myaggre.reset_index())
#myaggre = df.groupby(['Batch'])[['1']].mean()

#myaggre.plot()