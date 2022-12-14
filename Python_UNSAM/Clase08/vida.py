# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:10:08 2021

@author: Silvina Delgado
"""
from datetime import datetime

#%%
def vida_en_segundos(fecha_nac):
    '''
    Ingresar fecha_nac en formato dd/mm/AAAA.
    Devuelve la cantidad de segundos vividos
    '''
    #Convierto string en objeto datetime 
    t1 = datetime.strptime(fecha_nac, '%d/%m/%Y')
    #Obtengo fecha y hora actual
    t2 = datetime.now()
    sec = t2 - t1
    
    return float(sec.total_seconds())

#vida_en_segundos("01/05/1993")