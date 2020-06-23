# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:34:15 2020

@author: Paul
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
df=pd.read_excel(r'HIV_3.xlsx')
print(df)

print(df.isnull().sum())
ax=plt.figure(figsize=(10, 10))
ax.suptitle('A story, HIV prevalence in Nigeria (Omisoal, Idowu, 2020)')
#ax.annotate('Source: World bank (Created by Omisola, Idowu, 2020)', xy=(0.1, 0.02))


years=['2000','2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
x=years
print(x)
line=plt.plot
y=df['Adults_ages_15_plus_and_children_ages_0_14_newly_infected_with_HIV']
z=df['Number_of_neonatal_deaths']
a=df['Antiretroviral_therapy_coverage_%_of_people_living_with_HIV']
b=df['Prevalence_of_HIV_male_%_ages_15_24']
c=df['Prevalence_of_HIV_female_%_ages_15_24']
d=df['Prevalence_of_HIV_total_% _of_population_ages_15_49']
plt.subplot(221)
plt.xlabel('Changes over the years')
plt.ylabel('Occurence by population')
plt.xticks(rotation=90)
line(x,y, 'r', x, z, 'cyan', linewidth=5.0, animated=True, clip_on=True )
import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='New HIV prevalence among youths')
cyan_patch = mpatches.Patch(color='cyan', label='Neonatal deaths')
#blue_patch = mpatches.Patch(color='yellow', label='sIgM+IgG positive')
#orange_patch = mpatches.Patch(color='orange', label='site4')
#brown_patch = mpatches.Patch(color='brown', label='site5')
#black_patch = mpatches.Patch(color='black', label='site6')
plt.legend(handles=[red_patch, cyan_patch], loc=(0, 1))


plt.subplot(222)
plt.xlabel('Changes over the years')
plt.ylabel('Occurence by % of total population')
plt.xticks(rotation=90)
line(x,b, 'orange', x, c, 'magenta', linewidth=5.0 )
import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='orange', label='% Prevalence of HIV among males')
cyan_patch = mpatches.Patch(color='magenta', label='% Prevalence of HIV among females')
#blue_patch = mpatches.Patch(color='yellow', label='sIgM+IgG positive')
#orange_patch = mpatches.Patch(color='orange', label='site4')
brown_patch = mpatches.Patch(color='brown', label='% Total prevalence of HIV (ages 15-49)')
#black_patch = mpatches.Patch(color='black', label='site6')







plt.legend(handles=[red_patch, cyan_patch], loc=(0, 1))

plt.subplot(223)
plt.xlabel('Changes over the years')
plt.ylabel('Percentage cases of population')
plt.xticks(rotation=90)
bar_width=0.31
e=np.arange(len(a))
plt.bar(e+bar_width, a, width=bar_width, color='green', zorder=2)
plt.bar(e+bar_width*2, d, width=bar_width, color='magenta', zorder=2)
plt.xticks(e+bar_width*2,['2000','2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018'])
import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='green', label='% Antiretroviral therapy coverage')
cyan_patch = mpatches.Patch(color='magenta', label='% Total Prevalence of HIV')
#blue_patch = mpatches.Patch(color='yellow', label='sIgM+IgG positive')
#orange_patch = mpatches.Patch(color='orange', label='site4')
#brown_patch = mpatches.Patch(color='brown', label='site5')
#black_patch = mpatches.Patch(color='black', label='site6')







plt.legend(handles=[red_patch, cyan_patch], loc=(-0.05, -0.34))



plt.show()







