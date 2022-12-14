# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 15:12:10 2021

@author: Silvina
"""

#Ejercicio 11.11: Búsqueda binaria

def bbinaria_rec(lista, e):
    '''
    Dada una lista ordenada, 
    devuelve True si el elemento está en la misma y False si no
    '''
    if len(lista) == 0:
        res = False
    
    elif len(lista) == 1:
        res = lista[0] == e
    
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = True
        if lista[medio] > e:
            res = bbinaria_rec(lista[:medio], e)
        else:               
            res = bbinaria_rec(lista[medio:], e)
    
    return res