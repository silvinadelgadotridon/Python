# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:04:23 2021

@author: Silvina Delgado
"""
#Ejercicio 5.9: Empezando a plotear

import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas= np.load('../Data/temperaturas.npy')
    
    return plt.hist(temperaturas, color='turquoise', bins = 40)
   
    
plotear_temperaturas()
plt.title(" Valores de tempetura en 999 mediciones")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Frecuencia ")