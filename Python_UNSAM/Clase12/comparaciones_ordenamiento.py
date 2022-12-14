# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:59:51 2021

@author: Silvina
"""
import random
import numpy as np
import matplotlib.pyplot as plt

#%%

def generar_lista(N):
    lista = []
    [lista.append(random.randint(1,1000)) for i in range(N)]
    return lista

#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    cont = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        cont += n 
        # reducir el segmento en 1
        n = n - 1
        
    return cont

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    cont = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:    
        #print("DEBUG: ", lista)
            cont += reubicar(lista, i + 1)
        else:
            cont += 1

    return cont

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    cont = 1 #comenzamos con una comparacion
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        cont += 1
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return cont

#%%
def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
   
    n = len(lista)
    cont = 0
    while n > 1:  
        #n términos numerados del 0 al n-1
        for j in range(n-1): 
            #formo burbuja entre dos terminos seguidos
            if lista[j] > lista[j+1]:
                #si el primero es mayor que el segundo, se intercambian
                lista[j], lista[j+1] = lista[j+1], lista[j]
        cont += n-1
        n -= 1
                #print("DEBUG: ", n, j, lista)        
    return cont
    
#%%
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
        comp = 0
    else:
        medio = len(lista) // 2
        izq, comp_izq = merge_sort(lista[:medio])
        der, comp_der = merge_sort(lista[medio:])
        lista_nueva, comp_merge = merge(izq, der)
        comp = comp_izq + comp_der + comp_merge
    return lista_nueva, comp

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comp_aux = 0
    
    while(i < len(lista1) and j < len(lista2)):
        comp_aux += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comp_aux

#%%
def experimento(N, k):
    '''Devuelve una tupla con métodos de ordenamiento de listas
    (selección, inserción y burbujeo)'''
   
    lista =  generar_lista(N)
    seleccion = [ord_seleccion(lista.copy()) for _ in range(k)] 
    insercion = [ord_insercion(lista.copy()) for _ in range(k)]
    burbujeo = [ord_burbujeo(lista.copy()) for _ in range(k)]
    merge = [merge_sort(lista.copy())[1] for _ in range(k)]
    prom_selec = float(sum(seleccion)/k)
    prom_inser = float(sum(insercion)/k)
    prom_burb = float(sum(burbujeo)/k)
    prom_mer = float(sum(merge)/k)
    
    return prom_selec, prom_inser, prom_burb, prom_mer

#%%
def experimento_vectores(Nmax):
    '''Genera una lista de largo N 
    con números enteros del 1 al 1000 en orden aleatorio
    para N entre 1 y Nmax'''
    
    seleccion = []
    insercion = []
    burbujeo = []
    merge = []
    
    for N in range(Nmax):
        lista = generar_lista(N) 
        comparaciones_seleccion = ord_seleccion(lista.copy()) 
        comparaciones_insercion = ord_insercion(lista.copy())
        comparaciones_burbujeo = ord_burbujeo(lista.copy()) 
        comparaciones_merge = merge_sort(lista.copy())[1] 
        seleccion.append(comparaciones_seleccion)
        insercion.append(comparaciones_insercion)
        burbujeo.append(comparaciones_burbujeo)
        merge.append(comparaciones_merge)
    comparaciones_seleccion = np.array(seleccion) 
    comparaciones_insercion = np.array(insercion)
    comparaciones_burbujeo = np.array(burbujeo) 
    comparaciones_merge = np.array(merge)
    
    return comparaciones_seleccion, comparaciones_insercion, comparaciones_burbujeo, comparaciones_merge

       
#%%    
def grafico (Nmax):
    comp_seleccion, comp_insercion, comp_burbujeo, comp_merge = experimento_vectores(Nmax)    
    plt.figure(figsize=(7,5))
    plt.title('Cantidad de comparaciones') 
    plt.plot(comp_insercion, label = "Inserción")
    plt.plot(comp_seleccion, label = 'Selección', color = 'orange')
    plt.plot(comp_burbujeo,  linestyle=':', label = 'Burbujeo', color = 'black' )
    plt.plot(comp_merge, label = 'Merge sort', color = 'pink')
    plt.legend()
    return plt.show()

if __name__ == '__main__':
    grafico(256)
    