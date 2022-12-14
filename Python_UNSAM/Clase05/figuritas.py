# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:35:49 2021

@author: Silvina Delgado
"""
#%%
import random
import numpy as np

  
#%%

#Ejercicio 5.10: Crear

def crear_album(figus_total):
    a = np.zeros(figus_total)
    return a


#Ejercicio 5.11: Incompleto
    
def album_incompleto(a):
    if min(a) == 0:
        return True
    else:
        return False


#Ejercicio 5.12: Comprar

def comprar_figu(figus_total):
    return random.randint(0 , figus_total-1) 


#Ejercicio 5.13: Cantidad de compras    

def cuantas_figus(figus_total):
    numero = 0
    al= crear_album(figus_total)
    while album_incompleto(al):
        al[comprar_figu(figus_total)] += 1
        numero += 1
    
    return numero
        

#cuantas_figus(figus_total)     

#%%
#Ejercicio 5.14:
    
n_repeticiones = 1000
figus_total =6 

l =[cuantas_figus(figus_total) for n in range(n_repeticiones)]

lista_prom = np.mean(l)

n_repeticiones = 1000
figus_total =6 

#%%
#Ejercicio 5.15:

n_repeticiones = 100
figus_total =670     

def experimento_figus(n_repeticiones, figus_total):
    l = [cuantas_figus(figus_total) for n in range(n_repeticiones)]
    l_prom = np.mean(l)
    return l_prom
    
#experimento_figus(n_repeticiones, figus_total)    
