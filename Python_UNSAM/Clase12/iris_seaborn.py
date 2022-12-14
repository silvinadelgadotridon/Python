# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 01:03:25 2021

@author: Silvina
"""
import seaborn as sns
import matplotlib.pyplot as plt

#busqué en internet como aplicar la libreria seaborn

plt.figure()

df =sns.load_dataset('iris')
f = sns.pairplot(df, hue = 'species', kind='scatter', diag_kind='hist')

plt.show()


#%%
