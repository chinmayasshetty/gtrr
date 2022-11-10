# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 22:18:31 2022

@author: ASUS
"""

import pandas as pd
import matplotlib.pyplot as p
df=pd.read_csv("C:/Users/ASUS/Downloads/train.csv")
print(df)
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(len(df))
print(df.head(10))
print(df['Survived'].value_counts().plot(kind='bar'))
print(df[df['Sex']=='female']['Survived'].value_counts().plot(kind='bar'))
print(df[df['Pclass']==3]['Survived'].value_counts().plot(kind='bar'))
p.scatter(df['Fare'],df['Pclass'])
print(df[df['Sex']=='female']['Survived'].value_counts().plot(kind='pie'))

