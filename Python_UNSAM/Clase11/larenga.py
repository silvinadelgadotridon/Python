# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:36:50 2021

@author: Silvina
"""
def pascal(n, k):
    '''
    Calcula el valor que se encuentra en la fila n y columna k
    '''
    if k in (0, n):     
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)

