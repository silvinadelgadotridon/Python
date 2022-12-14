# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:33:48 2021

@author: Silvina
"""
#Ejercicio 12.2: burbujeo

def ord_burbujeo(lista):
    """Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
   
    n = len(lista)
    for i in range(n):
        #n términos numerados del 0 al n-1
        for j in range(0, n-1):
            #formo burbuja entre dos terminos seguidos
            if lista[j] > lista[j+1]:
                #si el primero es mayor que el segundo, se intercambian
                lista[j], lista[j+1] = lista[j+1], lista[j]
                #print("DEBUG: ", n, j, lista)
    return lista

#la complejidad de este algoritmo, en términos de rendimiento, depende de
#la lista base que se quiera ordenar, siendo el mejor caso, 
#la lista previamente ordenada (e.g. lista_2, donde el número 
#de intercambios es cero) y, el peor,
# la lista ordenada en orden inverso 
#(e.g. lista_4, donde el número de comparaciones como el de intercambios
#coinciden, por lo tanto son del orden de n cuadrado)   