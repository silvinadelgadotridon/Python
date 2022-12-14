# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:35:55 2021

@author: Silvina Delgado
"""
#%%
import sys
sys.argv
import csv
import fileparse
import lote
import formato_tabla 

#%%
def leer_camion(nombre_archivo):          
    """
    camion.csv tiene  nombres de frutas, 
    numero de cajones y precios de los productos 
    transportados
    """
    with open(nombre_archivo) as file:
        camion_dicts = fileparse.parse_csv(file, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

#leer_camion('../Data/camion.csv')

#%%


def leer_precios(nombre_archivo):
    #from fileparse import parse_csv
    with open(nombre_archivo) as file:
        precio = fileparse.parse_csv(file, types=[str, float], has_headers = False)
        precios = {}               
        
        for row in precio:
            precios[row[0]] = float(row[1]) 
        return precios
        
#leer_precios('../Data/precios.csv')

#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)
        

def hacer_informe(camion, precios):
    lista = []
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    
    for i in camion:
        #esta parte de código la copié de la versión dada por Manuela Cerdeiro porque me pareció
        #más simple a la que yo había realizado anteriormente
        if i.nombre in precios:
            precio_venta = precios[i.nombre]
            cambio = precio_venta - float(i.precio)
            t = (i.nombre, i.cajones, precio_venta, cambio)
            lista.append(t)              
    return lista
        
  

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
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
        
  




    