# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 01:10:25 2021

@author: Silvina
"""


def medidas_hoja_A(N):
    '''
    Devuelve una tupla (ancho, largo), representando el 
    tamaño de la hoja (medidas expresadas en mm) 
    '''
    ancho = 841
    largo = 1189
    if N == 0:
        return ancho, largo
    else:        
        res = medidas_hoja_A(N-1)
        return res[1]//2 , res[0]