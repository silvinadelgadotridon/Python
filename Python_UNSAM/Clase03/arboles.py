
#Silvina Delgado
#Ejercicio 3.18
#%%
import csv
import os
from typing import MutableMapping

def leer_parque(nombre_archivo, parque):
               
    
    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)       
        lista = []
        
        for row in rows:
            arbol = dict(zip(headers, row)) # creo pares clave/valor y construyo diccionarios.
            if arbol["espacio_ve"] == parque:
             
                lista.append(arbol)               #agrego elementos por cada ciclo                  
        
    return lista

parques = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
print(parques)
#len(parques)       #para general paz, me da 690


# %%
#Ejercicio 3.19
 
import csv

def especies(lista_arboles):
    lista = []

    for i in lista_arboles:
        lista.append(i['nombre_com'])
    return (set(lista))         #armo conjuntos con set

esp_arb = especies(parques) 
print(esp_arb)

#De acá en adelante, no se entregan
# %%
#Ejercicio 3.20
import csv 
from collections import Counter

def contar_ejemplares(lista_arboles):
    especie = Counter()     # usa los metodos primitivos del diccionario para implementar un contador. si no está la clave, defino un diccionario que empieza a contar la especie que aparece en la lista desde cero

    for arbol in lista_arboles:         
        especie[arbol['nombre_com']] +=1 #me suma la cantidad de veces que aparece la especie en la lista
        
    return especie      #me devuelve un diccionario key= nombre de la especie: value= cantidad


parques1 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
ejemplares1 = contar_ejemplares(parques1) 
print(f'--'*20)
print( 'General Paz')
print(f'--'*20)
for i,j in ejemplares1.most_common(5):
    print(f'{i:<3s}: {j:>3d}')
print('')

parques2 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
ejemplares2 = contar_ejemplares(parques2) 

print(f'--'*20)
print( 'Los Andes')
print(f'--'*20)
for i,j in ejemplares2.most_common(5):
    print(f'{i:<3s}: {j:>3d}')
print('\n')

parques3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
ejemplares3 = contar_ejemplares(parques3)

print(f'--'*20) 
print(  'Centenario')
print(f'--'*20)
for i,j in ejemplares3.most_common(5):
    print(f'{i:<3s}: {j:>3d}')
print('\n')

#%%
#Ejercicio 3.21
import csv


def leer_parque(nombre_archivo, parque):
    lista = []

    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)       
        
        for row in rows:
            arbol = dict(zip(headers, row)) # creo pares clave/valor y construyo diccionarios.
            arbol['altura_tot'] = float(arbol['altura_tot'])
            if arbol['espacio_ve'] == parque:
                lista.append(arbol)               #agrego elementos por cada ciclo                  
        
    return lista

parques = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')

#%%

def obtener_alturas(lista_arboles, especie):
    lista = []

    for arbol in lista_arboles:
        if especie == arbol['nombre_com']:
            lista.append(arbol['altura_tot'])
    return lista

altura_jacaranda = obtener_alturas(parques, 'Jacarandá') 
print (altura_jacaranda)

maximo = max(altura_jacaranda)
promedio = round(sum(altura_jacaranda)/len(altura_jacaranda), 2)
print('El máximo es:', maximo, 'y el promedio:', promedio)          
        
# %%
#Ejercicio 3.22: Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    lista = []

    for arbol in lista_arboles:
        
        inclinacion = arbol['inclinacio']
        if especie in arbol['nombre_com']:
            
            lista.append(inclinacion)
    return lista

parques3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
inclinaciones = obtener_inclinaciones(parques3,'Falso Guayabo')
print(inclinaciones) 


# %%
#Ejercicio 3.23: Especie con el ejemplar más inclinado
import csv

def especimen_mas_inclinado(lista_arboles):          
    lista =[]
    listita =[]
    
    for arbol in lista_arboles:
        nombre =arbol['nombre_com']
        inclinacion = int(arbol['inclinacio'])  #los valores de inclinacion son enteros
        listita = [nombre, inclinacion] #creo lista con dos elementos
        lista.append(listita)       #armo una lista de listas
    idx, max_incl= max(lista, key=lambda item: item[1]) #calculo el valor máximo de todas las listas
    return idx, max_incl    #devuelvo el nombre del arbol y el maximo

parques3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
mas_incli = especimen_mas_inclinado(parques3)
print(mas_incli)

#%%
#Ejercicio 3.24: Especie más inclinada en promedio
import statistics
from collections import Counter

def especie_promedio_mas_inclinada(lista_arboles):
    dic = {}
    lista = []
    nombre = Counter () 

    for arbol in lista_arboles:
        nombre =arbol['nombre_com']
        inclinacion = int(arbol['inclinacio'])  #los valores de inclinacion son enteros
        
        listita = [nombre, inclinacion] #creo lista con dos elementos
        lista.append(listita)
    
        
        for nombre in lista:
            nombre[arbol['nombre_com']] +=1
    
    return set(lista)

parques3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
mas_incli_prom = especie_promedio_mas_inclinada(parques3)
print(mas_incli_prom)

#%%
        
            
    
    mean = sum(inclinacion)/especie
    idx, max_incl= max(mean, key=lambda item: item[1]) #calculo el valor máximo de todas las listas
    return idx, max_incl    #devuelvo el nombre del arbol y el maximo

parques3 = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
mas_incli_prom = especie_promedio_mas_inclinada(parques3)
print(mas_incli)
            


#%%        
Metí cada nombre de árbol en un diccionario con valor 
[suma de las inclinaciones, cantidad de árboles con ese nombre, parque]
Despues dividis la suma de las inclinaciones x el total de arboles con 
ese bombre        


#%%




# %%
