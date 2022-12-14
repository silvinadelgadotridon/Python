# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:24:42 2021

@author: Silvina Delgado
"""
#Ejercicio 5.1: Generala servida

import random


def tirar():
    tirada = []
    [tirada.append(random.randint(1,6)) for i in range(5)]
    return tirada


def es_generala(tirada):
   
    return max(tirada) == min(tirada)
    

                
N = 1000000
generala_servida = [es_generala(tirar()) for i in range (N)]    
G = sum(generala_servida)
prob = G/N 

print(f"Tiré {N}, de las cuales {G} saqué generala")
print(f"La probabilidad de hacer generala tirada es de {prob}")


#%%
#Ejercicio 5.2: Generala no necesariamente servida

from collections import Counter

def prob_generala(N):
    
    tirada = []
    [tirada.append(random.randint(1,6)) for i in range(5)]
    
    if max(tirada) == min(tirada):
        return True
    else:
        tirada_2 = Counter(tirada).most_common()[0]
        tirada = [i for i in tirada if i==tirada_2]
        [tirada.append(random.randint(1,6)) for i in (range(5 - len(tirada)))]
        
        if max(tirada) == min(tirada):
            return True    
        
        else:
            tirada_3 = Counter(tirada).most_common()[0]
            tirada = [i for i in tirada if i==tirada_3]
            [tirada.append(random.randint(1,6)) for i in (range(5 - len(tirada)))]
        
            if max(tirada) == min(tirada):
                return True    
            
            else: 
                return False
    
    return tirada

N = 1000000
generala_servida = [prob_generala(N) for i in range (N)]    
G = sum(generala_servida)
prob = G/N 

print(f"Tiré {N}, de las cuales {G} saqué generala")
print(f"La probabilidad de hacer generala en tres tirada es de {prob}")

#%%
#Hecho en clase
import random

def tirar(cant_dados):
            return [random.randint(1,6) for _ in range(cant_dados)]

def es_generala(tirada):
    return tirada.count(tirada[0]) == 5

def cuantos_cada_cara(dados_en_mesa):
    return sorted([( dados_en_mesa.count(d), d) for d in range(1 , 6+1)], reverse = True)
    
def varias_manos():
    manos = 3
    mesa = []
    
    for i in range(manos):
        mesa = mesa + tirar(5 - len(mesa))
        if i < manos - 1:
            (cant, valor) = cuantos_cada_cara(mesa)[0]
            mesa = [valor] *cant
    
    return mesa

def experimentar_prop_generada(n):
    ganadas = sum([es_generala(varias_manos()) for _ in range (n)])
    probabilidad = ganadas/n
    return probabilidad

#ganadas = sum([es_generala(tirar(5)) for _ in range (n_tiradas)])

def experimentar_cantidades(n):
    resultados =[ varias_manos() for _ in range(n)]
    return resultados

res = experimentar_cantidades(1000)

import matplotlib.pyplot as plt

maximo_repetido = [cuantos_cada_cara(r)[0][0] for r in res]
plt.hist(maximo_repetido, bins  = [0.5 , 1.5 , 2.5 , 3.5 , 4.5 , 5.5], edgecolor= "black" )
plt.xticks([1, 2, 3, 4, 5])
plt.xlim(0 , 6)
plt.xlabel("Cantidad máxima de repeticiones")
plt.ylabel("Cantidad de observaciones")
    

#%%
import random

random.seed(31415) #fijo numero entero

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada) #la secuencia de números aleatorios va a ser reproducible utilizando la misma semilla.

#%%
#La función random.choice() toma una secuencia y devuelve un elemento aleatorio
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras)) 

#%%
#Ejercicio 5.3: Cocumpleaños

#TERMINAR

import random

from collections import Counter


cocumple = []
dias = list(range(365)) 
N = list(range(10))

for i in N:
    cocumple.append(random.choices(dias,k =30))

G = Counter(cocumple).most_common()
prob = G/N 

#%%
#Ejercicio 5.4: Envido

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
random.sample(naipes,k=3) #sin reposicion

#%%
import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#%%
#Ejercicio 5.6: Gaussiana

import random


def medir_temp(n):
    lista = []
    for i in range(n):
        dis_norm = random.normalvariate(0,0.2)
        lista.append(dis_norm + 37.5)
    
    maxim = max(lista)
    minim = min(lista)
    promedio = sum(lista)/n
    q1 = (sorted(lista))[25]
    q3 = (sorted(lista))[75]
    def median(lista):
        datos = sorted(lista) #ordeno lista
        if len(datos) % 2 == 0:     #si es par
            n = len(datos)      
            mediana = (datos[n / 2 - 1] + datos[n / 2]) / 2 #promedio los datos centrales
        else:   #impar
            mediana = datos[len(datos) / 2] #tomo el valor central
        
    
        
    return maxim, minim, promedio, q1, q3 mediana
      




#%%

#Ejercicio 5.7: arange() y linspace()
import numpy as np
#primer número, el límite, y el paso.
np.arange(1, 20, 2)
#primer número, el último número, y la cantidad de elementos
np.linspace(1, 19, num=10)
#diferencia entre métodos: linspace devuelve elementos del array como flotantes

 
#%%
import numpy as np

data = np.array([1, 2, 3])

#%%
#Ejercicio 5.8: Guardar temperaturas

#%%












