# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:55:55 2021

@author: Silvina Delgado
"""
#%%
import random
import matplotlib.pyplot as plt
import numpy as np

#%%
def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 
        pos = i
        break
    return pos, comps


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        medio = (izq + der) // 2   
        comps += 1
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio    
        if lista[medio] > x:
            der = medio - 1 
        else:             
            izq = medio + 1
    return pos, comps

#%%
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l


def generar_elemento(m):
    return random.randint(0, m-1)


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom


#%%
def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(256) + 1 
    comps_promedio = np.zeros(256) 
    comps_prome = np.zeros(256)

    for i, n in enumerate(largos):
        lista = generar_lista(n, m) 
        comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)
        comps_prome[i] = experimento_binario_promedio(lista, m, k)

    plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
    plt.plot(largos,comps_prome,label = 'Búsqueda Binaria')
    plt.xlim([0,100])
    plt.xlabel("Largo de la lista")
    plt.ylim([0,50])
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    
    return plt.show()