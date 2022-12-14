# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:35:55 2021

@author: Silvina Delgado
"""
#%%
import csv
from fileparse import parse_csv

#%%
def leer_camion(nombre_archivo):          
    
    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        """
        camion.csv tiene  nombres de frutas, 
        numero de cajones y precios de los productos 
        transportados
        """
        lista = parse_csv(nombre_archivo, types=[str, int, float])
    
    return lista

#leer_camion('../Data/camion.csv')

#%%


def leer_precios(nombre_archivo):
    
    """
        precios.csv tiene precios de venta
        y nombres de frutas y verduras,
    """
    
    with open(nombre_archivo, 'rt',encoding= 'utf8') as f:              
        precios = parse_csv(nombre_archivo, types=[str,float], has_headers=False)
        
      
        return dict(precios)
        
#leer_precios('../Data/precios.csv')

#%%

def hacer_informe(camion, precios):
    lista = []
    listita = []
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    for i in camion:
         if i['nombre'] in precios:
             listita.append(i['nombre'])
             listita.append(int(i['cajones']))
             listita.append(float(i['precio']))
             cambio = precios[i['nombre']]- float(i['precio'])
             listita.append(cambio)
             lista.append(listita)
             listita = []
                   
    for i in headers:
                
        print(f'{i:>10s}', end = ' ' )
    print('\n')
                
    print(f'---------- ---------- ---------- ----------', end = '\n')
        
    for nombre, cajones, precio, cambio in lista:
        precio_1 = f'${round(precio, 2)}'
        print(f'{nombre:>10s} {cajones:>10d} {precio_1:>10s} {cambio:>10.2f}')



#%%

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    
    def imprimir_informe(informe):
        return informe 
    
    informe = hacer_informe(camion, precios)
    
    return imprimir_informe(informe)

#informe_camion('../Data/camion.csv', '../Data/precios.csv')


    
        
  




    