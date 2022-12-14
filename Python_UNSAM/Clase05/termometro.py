# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:35:45 2021

@author: Silvina Delgado
"""
#Ejercicios 5.6 y 5.8


import random
import numpy as np


def medir_temp(n):
    lista = []
    for i in range(n):
        dis_norm = random.normalvariate(0,0.2)
        lista.append(dis_norm + 37.5)
        
    vector = np. array(lista)
    np.save('../Data/temperaturas.npy', vector)
    
    return lista

medir_temp(999)

np.load('../Data/temperaturas.npy')

#%%

def resumen_temp(n):  
    lista = medir_temp(n)
    maxim = max(lista)
    minim = min(lista)
    promedio = sum(lista)/n
    
    datos = sorted(lista) #ordeno lista  
    mitad = int(n / 2)
    mediana = (datos[mitad])  #tomo el valor central
   
            
    return round(maxim,2), round(minim, 2), round(promedio,2), round(mediana,2)

resumen_temp(999)
