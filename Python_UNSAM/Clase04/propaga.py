# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:07:06 2021

@author: Silvina Delgado
"""
        

#%%
# EJERCICIO 4.6: Propagación

def propagar(lista):
    
    l = len(lista)-1
    
    for n,i in enumerate(lista):
    
        if i == 1 and n<l:
                              
            if lista[n+1] == 0:
                lista[n+1] = 1
                
            if lista[n+1] == -1:
                lista[n+1] = -1
                
        
    n = len(lista)
    while n > 0:
        if lista[n-1] == 0 and lista[n] == 1:
                lista[n-1]= 1
        n -= 1
    
    return lista

#%%

#Solución hecha en clase:
    
def propagar(lista):
    
    l = len(lista)
    cambio = True
    
    while cambio:
        cambio = False
    
        for n,i in enumerate(lista):
    
            if i == 1:
                if n > 0 and lista[n-1] == 0:
                    cambio = True
                    lista[n-1]= 1
                if n< l-1 and lista[n+1] == 0:
                    cambio = True
                    lista[n+1]= 1
    
    return lista
           
    
                
                
            
    