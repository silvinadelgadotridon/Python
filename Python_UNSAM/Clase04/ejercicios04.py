# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:58:08 2021

@author: Silvina Delgado
"""

def geringoso(cadena):
    gerin = ''
    for letra in cadena:
        gerin += letra
        if letra in 'aeiou':
            gerin += 'p' + letra
    return(gerin)

#%%
#Programacion por contratos
def add(x, y):
    assert isinstance(x, int), 'Necesito un entero (int)'
    assert isinstance(y, int), 'Necesito un entero (int)'
    return x + y

#%%
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

rta = tiene_a ('palabra')
print(rta)

#%%
#Ejercicio 4.1
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1     
        invertida.append (lista.pop(i))  #pop elimina el elemento i de la lista
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

#%%
#Ejercicio 4.2

import csv


from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    registro = {}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

#%%
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:  # recorremos los elementos de la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        i += 1       
    return pos
#%%
#Aca uso enumerate
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

#%%
#Ejercicio 4.7: Comprensión de listas

nums = [1,2,3,4]
cuadrados = [x * x for x in nums]
cuadrados

dobles = [2 * x for x in nums if x > 2]
dobles

#%%
#Ejercicio 4.8: Reducción de secuencias
import os
import csv

def leer_camion(nombre_archivo):
    camion = {}
    lista = []           
    
    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in f:
            try:
                row = line.split(',')
                row[2] = row[2].rstrip()
                record = dict(zip(headers, row)) 
                lista.append(record)
                camion = {}                                               
        
            except ValueError:
                print(f' No pude interpretar: {row}')     
    
    return lista

camion = leer_camion('../Data/camion.csv')

costo = sum([int(s['cajones']) * float(s['precio']) for s in camion])
 
#%%

def leer_precios(nombre_archivo):
    
    with open(nombre_archivo, 'rt',encoding= 'utf8') as f:
        rows = csv.reader(f)
        precios = {}               
        
        for i, row in enumerate(rows):
            try:
                precios[row[0]] = float(row[1]) 
                #print(i+1,row)
            
            except:                    
                print(f'lista vacía {i+1}:{row}')

        return precios

precios = leer_precios('../Data/precios.csv')

valor = sum([int(s['cajones']) * precios[s['nombre']] for s in camion])

#%%
#Ejercicio 4.9: Consultas de datos

mas100 = [s for s in camion if int(s['cajones']) > 100]    

myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]

costo10k = [s for s in camion if int(s['cajones']) * float(s['precio']) > 10000]


#%%
#Ejercicio 4.10: Extracción de datos

nombre_cajones =[(s['nombre'], s['cajones']) for s in camion] #construyo lista de tuplas 

nombres = {s['nombre'] for s in camion} #listado de comprension de conjuntos

stock = {nombre: 0 for nombre in nombres} #especificando clave/valor creo comprension de diccionario
for s in camion:        #al cero del value, le doy el valor de los cajones
    stock[s['nombre']] += int(s['cajones'])

camion_precios = {nombre: precios[nombre] for nombre in nombres} #creo dicc de precios de venta de los productos cargados en el camion

#%%
#Ejercicio 4.11: Extraer datos de un archivo CSV

import csv
f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
select = ['nombre', 'cajones', 'precio']

indices = [headers.index(ncolumna) for ncolumna in select]

row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}   # comprensión de diccionario

camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]

#Ejercicio 4.12: Datos de primera clase

import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
types = [str, int, float]
row = next(rows)
r = list(zip(types, row))
types[1](row[1])*types[2](row[2])

converted = []
for func, val in zip(types, row):
          converted.append(func(val))


#Ejercicio 4.13: Diccionarios
dict(zip(headers, converted))

{ name: func(val) for name, func, val in zip(headers, types, row) } # o con comprension de dic


#%%
#Ejercicio 4.14: Fijando ideas

import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

def tupla_fe(fecha):
    tupla = tuple(int(s) for s in fecha.split('/') ) #armo una tupla con comprension, teniendo en cuenta que el texto esta separado por /
    return tupla

types = [str, float, tupla_fe, str, float, float, float, float, int]    #añado la funcion a lla posicion de la fila date, que antes era una string
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))



































