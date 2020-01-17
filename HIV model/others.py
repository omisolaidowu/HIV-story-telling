'''
-*- coding: utf-8 -*-
Created on Fri Jan 17 12:34:15 2020

@author: Paul
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
df=pd.read_excel(r'C:\Users\Paul\Desktop\Python projects\HIV_3.xlsx')
print(df)

print(df.isnull().sum())
ax=plt.figure(figsize=(8, 8))
years=['2000','2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
x=years
print(x)
line=plt.plot
y=df['']
z=df['Number_of_neonatal_deaths']
plt.xlabel('Changes over the years')
plt.ylabel('Occurence by population')
plt.xticks(rotation=90)
line(x,y, 'r', x, z, 'cyan' )
import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='New HIV prevalence among youths')
cyan_patch = mpatches.Patch(color='cyan', label='Neonatal deaths')
#blue_patch = mpatches.Patch(color='yellow', label='sIgM+IgG positive')
#orange_patch = mpatches.Patch(color='orange', label='site4')
#brown_patch = mpatches.Patch(color='brown', label='site5')
#black_patch = mpatches.Patch(color='black', label='site6')





plt.legend(handles=[red_patch, cyan_patch], loc=(0, 1))

plt.show()

