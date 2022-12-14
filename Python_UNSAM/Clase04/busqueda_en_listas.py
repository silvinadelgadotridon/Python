# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:10:27 2021

@author: Silvina Delgado
"""
# EJERCICIO 4.3: Búsquedas de un elemento

def buscar_u_elemento(lista, e):
    pos = -1 
    
    for i, z in enumerate(lista):
        if z == e:   
            pos = i  
           
    return pos


def buscar_n_elemento(lista, e):
    contar = 0
    pos = -1 
    
    for i, z in enumerate(lista):
        if z == e:   
            pos = i 
            contar += 1
           
    return contar

#%%
# EJERCICIO 4.4: Búsqueda de máximo y mínimo
def maximo(lista):
    
    max = lista [0]

    for e in lista:
        if e >= max:
            max = e
    
    return max



def minimo(lista):
    
    min = lista [0]

    for e in lista:
        if e <= min:
            min = e
    
    return min