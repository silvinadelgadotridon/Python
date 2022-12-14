# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 14:11:09 2021

@author: Silvina Delgado

"""
#%%
# EJERCICIO 4.5: Invertir una lista



def invertir_lista(lista):
    invertida = []
    
    for e in lista:

        invertida = [e] + invertida
        
    return invertida

