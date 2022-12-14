# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:56:34 2021

@author: Silvina Delgado
"""
#Ejercicio 6.1: ropagar vecinos

def propagar_al_vecino(l):
    modif = False
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m

#es un algoritmo cuadratico
#%%

'''
Preguntas:

1. ¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino
 no causan un IndexError en los bordes de la lista?
Por la primer condición.. i <n-1 and i >0

2. ¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]),
 siendo entradas perfectamente simétricas, no generan la 
 misma cantidad de repeticiones de llamadas a la función 
 propagar_al_vecino?
porque el programa necesita reconocer un 0 para cambiar
un valor. Lo hace al final del largo de la lista.
En cambio en el segundo lo hace desde el principio
 
 
3. Sobre la complejidad. Si te sale, calculá:
¿Cuántas veces como máximo se puede repetir el ciclo 
while en una lista de largo n?
n-1

¿Cuántas operaciones hace "propagar_al_vecino" en una 
lista de largo n?
n-2
Entonces, ¿cuántas operaciones hace como máximo esta 
versión de propagar en una lista de largo n? 
¿Es un algoritmo de complejidad lineal o cuadrática?
'''
#%%
#Ejercicio 6.2: Propagar por como el auto fantástico

def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%
def propagar_a_izquierda(l):
    return propagar_a_derecha(l[::-1])[::-1]
#%
def propagar(l):
    m = l.copy() #agregue copy lista
    ld=propagar_a_derecha(m)
    lp=propagar_a_izquierda(ld)
    return lp


l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Propagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

#es un algoritmo lineal

#%%
#Ejercicio 6.3: Propagar con cadenas

def trad2s(l):
    '''traduce una lista con 1,0 y -1 
    a una cadena con 'f', 'o' y 'x' '''
    d={1:'f', 0 :'o', -1:'x'}
    s=''.join([d[c] for c in l])
    return s

def trad2l(ps):
    '''traduce cadena con 'f', 'o' y 'x'
    a una lista con 1,0 y -1'''
    inv_d={'f':1, 'o':0, 'x':-1}
    l = [inv_d[c] for c in ps]
    return l

def propagar(l, debug = True):
    s = trad2s(l)
    if debug:
        print(s, end = ' -> ') #descomenté esto
    W=s.split('x')
    PW=[w if ('f' not in w) else 'f'*len(w)+ "x" for w in W] #agregué + "x"
    ps=''.join(PW)
    if debug:
        print(ps)
    return trad2l(ps)


l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
lp = propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

#creo que es un algoritmo lineal

#%%

#Ejemplo

def leer_precios(nombre_archivo):
    precios = {}
    with open(nombre_archivo) as f:
        f_csv = csv.reader(f)
        for linea in f_csv:
            precios[linea[0]] = float(linea[1])
    return precios

preciosviejos = leer_precios('preciosviejos.csv')
preciosnuevos = leer_precios('preciosnuevos.csv')

#%%
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers == True:
        # Lee los encabezados del archivo
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []

            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
            # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
            
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]

            # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        
        else:
            indices = []

            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
            # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
            
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]

            # Armar el diccionario
                registro = tuple(fila)
                registros.append(registro)

    return registros

camion = parse_csv('../Data/camion.csv', types=[str, int, float])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)


#%%
import informe_funciones

#%%
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    comps = 0
    while izq <= der:
        medio = (izq + der) // 2    #SI PONGO UNA SOLA BARRA ME DA ERROR:significa que está pasando un flotante al código de formato esperando un número entero
        comps += 1
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps

#%%
#Ejercicio 6.14
def donde_insertar(lista, x):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''

    pos = -1 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2   
        if lista[medio] <= x: #modifique para que sea >=
            pos = medio + 1    #+1 para que me devuelva la posicion
        if lista[medio] > x:
            der = medio - 1 
        else:              
            izq = medio + 1 
    return pos
#%%
def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

