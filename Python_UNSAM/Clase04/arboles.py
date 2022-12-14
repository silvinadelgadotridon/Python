# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:47:26 2021

@author: Silvina Delgado

"""
#EJERCICIO 4.15: Lectura de todos los árboles
#%%

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

#%%

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)       
        arboleda = [ dict(zip(headers, row)) for row  in rows]
    
    return arboleda
    
nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)


#%%        
        
# EJERCICIO 4.16: Lista de altos de Jacarandá


H = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]    



#%%

#EJERCICIO 4.17: Lista de altos y diámetros de Jacarandá


lista = [(s['diametro'], s['altura_tot']) for s in arboleda if s["nombre_com"] == "Jacarandá"] 


#%%
#EJERCICIO 4.18: Diccionario con medidas


especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

        
diccionario = { clave: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == clave] for clave in especies }

#%%

#EJERCICIO 5.25: Histograma de altos de Jacarandás


H = [float(arbol['altura_tot']) for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]    

plt.figure()
plt.hist(H,color='turquoise', bins = 60)
plt.xlabel("Altura (m)")
plt.ylabel("Frecuencia")
plt.title("Histograma para alturas de Jacarandás") 

#%%
#EJERCICIO 5.26: Scatterplot (diámetro vs alto) de Jacarandás

def scatter_hd(lista_de_pares):
    altura = [(float(s['altura_tot'])) for s in arboleda if s["nombre_com"] == "Jacarandá"] 
    diametro = [(float(s['diametro'] )) for s in arboleda if s["nombre_com"] == "Jacarandá"] 
    d = np.array(diametro) 
    h = np.array(altura)
    plt.figure()
    plt.scatter (d,h, c='lightseagreen', alpha = 0.3)
    plt.xlabel("diametro (cm)")
    plt.xlim(0,150)
    plt.ylabel("altura (m)")
    plt.ylim(0,40)
    plt.title("Relación diámetro-alto para Jacarandás") 
    return plt.show()

   