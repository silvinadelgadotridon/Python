# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:02:41 2021

@author: Silchu
"""
def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    if n == 1:
        return 1
    return (n * factorial(n - 1))

f = factorial(10)
#%%
def sumar(lista):
    """Devuelve la suma de los elementos en la lista."""
    suma = 0    # parámetro suma que no forma parte del problema inicial
    while lista:
        lista, suma = lista[1:], lista[0] + suma
    return suma

sumar([1,2,5])

#%%
#cuerpo base de la funcion promediar
def promediar(lista):
    if len(lista) == 1:
        res = lista[0]
    else:
        res = promediar(lista[1:])
    return res

#%%
def promediar_aux(lista):   #firma natural de la función promediar()
    suma = lista[0]
    cantidad = 1    
    if len(lista) > 1:
        suma_resto, cantidad_resto = promediar_aux(lista[1:])
        suma += suma_resto
        cantidad += cantidad_resto
    return suma, cantidad

#%%
def promediar(lista):
    """Devuelve el promedio de los elementos de una lista de números."""

    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1    
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad

    suma, cantidad = promediar_aux(lista)
    return suma / cantidad

#%%
#Ejercicio 11.2: Números triangulares

def triangular(n):
    """Precondición: n entero positivo
       Devuelve: suma triangular de n!"""
    if n == 1:
        return 1
    else:
        return int(n*(n+1)/2)

#%%
#Ejercicio 11.3: Dígitos

def cant_digitos(n):
    '''Recibe numero positivo y devuelve cantidad de digitos'''
    if n < 10:
        return 1
    else:
        return 1 + cant_digitos(n / 10)

#%%
#Ejercicio 11.4: Potencias

def es_potencia(n, b):
    ''' recibe 2 enteros, n y b
    devuelve True si n es potencia de b y False si no'''
    if n == 1:
        return True
    if n < b:
        return False
    else:
        return es_potencia(n/b, b)

#%%
#Ejercicio 11.5: Subcadenas
def posiciones(a, b):
    '''recibe dos cadenas a y b,  
    devuelve una lista con las posiciones en donde se encuentra b dentro de a.
    '''    



#%%
def pascal(n, k):
    if k in (0, n):     
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)


def imprime():
    print("\n".join(["{:^40}".format("  ".join([f'{pascal(n,k)}' for k in range(n+1)])) for n in range(10)]))  



























