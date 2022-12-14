# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:58:10 2021

@author: Silvina Delgado
"""


#%%
#Ejercicio 6.15
def insertar(lista, x):
    '''
    Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    pos = -1 
    izq = 0
    der = len(lista) - 1
    if x in lista:
        while izq <= der:
                medio = (izq + der) // 2   
                if lista[medio] == x:
                    pos = medio    
                    return pos
                    break
                if lista[medio] > x:
                    der = medio - 1 
                else:              
                    izq = medio + 1 
    else:
        while izq <= der:
            medio = (izq + der) // 2   
            if lista[medio] <= x:
                pos = medio + 1    
            if lista[medio] > x:
                der = medio - 1 
            else:              
                izq = medio + 1 
    lista.append(x)
        
    return pos