# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:05:39 2021

@author: Usuario
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()


def ploteo(N,k=12,plotlim=1000):
    '''Hace el ploteo de k iteraciones de la funcion randomwalk'''

    
    fig = plt.figure(figsize=(9, 5), dpi=200)
    max=0
    min=N
    min_walk=None
    max_walk=None
    absarray=None
    for i in range(k):
        
        plt.subplot(2, 1, 1) # define la figura de arriba
        walk=randomwalk(N)
        absarray=np.abs(walk)# array con valores absolutos
        
        if min>=np.mean(absarray):# para ver el que menos se aleja se realiza la media del array de absolutos
            min=np.mean(absarray)
            min_walk=walk
            print(min)
        if max<=absarray[absarray.argmax()]:# para ver el que mas se aleja veo el maximo valor en el array absoluto
            max=absarray[absarray.argmax()]
            max_walk=walk

        plt.plot(walk)
    # Rango del eje x e y
    plt.ylim(-plotlim, plotlim)
    plt.xticks([])
    plt.yticks([-plotlim//2,0,plotlim//2])
    plt.title(f"{k} caminatas al azar", fontsize=10)
    plt.ylabel("Distancia al origen", fontsize=9)
    plt.xlabel("Tiempo", fontsize=9)

    plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
    plt.plot(max_walk)
    # Rango del eje x e y
    plt.ylim(-plotlim, plotlim)
    plt.xticks([])
    plt.yticks([-plotlim//2,0,plotlim//2])
    plt.title("Caminata que más se aleja", fontsize=10)

    plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
    plt.plot(min_walk)
    # Rango del eje x e y
    plt.ylim(-plotlim, plotlim)
    plt.xticks([])
    plt.yticks([-plotlim//2,0,plotlim//2])
    plt.title("Caminata que menos se aleja", fontsize=10)

    plt.show()

N = 100000
ploteo(N)