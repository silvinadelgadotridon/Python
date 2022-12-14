# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:06:54 2021

@author: Silvina Delgado
"""
#Ejercicio 7.10: Funciones y documentación

#%%
def valor_absoluto(n):
    '''Devuelve valor absoluto de un número real'''
    if n >= 0:
        return n
    else:
        return -n
    
#%%
def suma_pares(l):
    '''Devuelve la suma de elementos enteros que se encuentran en una
    secuencia iterable de tipo tupla o lista'''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
            # Si el elemento es par, lo sumo al resultado 
        else:
            res += 0
            # Si es impar, no el elemento no es sumado
    return res

#Invariante: res contiene la suma de enteros pares de la porción de lista que ya fue analizada.
#%%
def veces(a, b):
    '''Para dos números a (perteneciente a los reales) y b (perteneciente a los enteros positivos),
    esta función devuelve el producto de estos números'''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        # El print muestra el producto entre las variables a y b, b veces
        res += a
        nb -= 1
    return res

#Invariante: res contiene el producto de a y b
#%%
def collatz(n):
    '''Para n = número entero positivo, esta función devuelve la cantidad de iteraciones
    hasta converger a 1 a través de la conjetura Collatz'''
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2
            #Si n es par, se divide por 2
        else:
            n = 3 * n + 1
            #Si n es impar, se multiplica por 3 y se suma 1.
        res += 1
    return res

#Invariante: res, el cual es número de iteraciones. Como la variable comienza en 1,
#queda el número de pasos + 1 hasta converger a 1 