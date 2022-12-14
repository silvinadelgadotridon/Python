# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:35:55 2021

@author: Silvina Delgado
"""
#%%
import sys
sys.argv
import csv
from fileparse import parse_csv

#%%
def leer_camion(lines):          
    """
    camion.csv tiene  nombres de frutas, 
    numero de cajones y precios de los productos 
    transportados
    """
    for line in lines:
        lista = parse_csv(lines, types=[str, int, float])
    
        return lista

#leer_camion('../Data/camion.csv')

#%%


def leer_precios(lines):
    
    """
        precios.csv tiene precios de venta y nombres de frutas y verduras
    """   
    for line in lines:          
        precios = parse_csv(lines, types=[str,float], has_headers=False)
         
    return dict(precios)
        
#leer_precios('../Data/precios.csv')

#%%

def hacer_informe(camion, precios):
    lista = []
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    for i in camion:
        #esta parte de código la copié de la versión dada por Manuela Cerdeiro porque me pareció
        #más simple a la que yo había realizado anteriormente
        precio_venta = precios[i['nombre']]
        cambio = precio_venta - i['precio']
        t = (i['nombre'], i['cajones'], precio_venta, cambio)
        lista.append(t)              
         
    for i in headers:         
        print(f'{i:>10s}', end = ' ' )
        
    print('\n')           
    print(f'---------- ---------- ---------- ----------', end = '\n')
        
    for nombre, cajones, precio, cambio in lista:
        precio_1 = f'${round(precio, 2)}'
        print(f'{nombre:>10s} {cajones:>10d} {precio_1:>10s} {cambio:>10.2f}')


#%%

def informe_camion(lines_camion, lines_precios):
    
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    
    def imprimir_informe(informe):
        return informe 
    
    informe = hacer_informe(camion, precios)
    
    return imprimir_informe(informe)

#informe_camion('../Data/camion.csv', '../Data/precios.csv')


#%%
#Ejercicios 7.4, 7.5

def f_principal(argv):
    
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    camion = leer_camion(argv[1])
    precios = leer_precios(argv[2])
    informe = hacer_informe(camion, precios)
    return informe
      
    
if __name__ == '__main__':
    f_principal(sys.argv)
        
  




    