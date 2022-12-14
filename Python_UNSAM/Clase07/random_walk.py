# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 09:09:49 2021

@author: Silvina Delgado
"""
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

   
#Para determinar las trayectorias qye se aleja más y menos del origen
#me guié del código de la clase 7
N = 100000    
dist_max = -1
dist_min = N+1

for _ in range(12):
    caminata = randomwalk(N)
    dist = max(abs(caminata))
    
    if dist > dist_max:
        lejano = caminata
        dist_max = dist
        
            
    if dist < dist_min:
        cercano = caminata
        dist_min = dist
        
fig = plt.figure(figsize=(10, 6), dpi=300)

for i in range(12):   
    
    plt.subplot(2, 1, 1) # define la figura de arriba
    plt.plot(randomwalk(N))
    plt.xlim([-100,105000])
    plt.xticks([])
    plt.ylim([-900,900])
    plt.yticks([-500, 0, 500], [r'$-500$', r'$0$', r'$+500$'])
    plt.title("12 caminatas al azar", fontsize=10)
    plt.ylabel("Distancia al origen", fontsize=10)
    plt.xlabel("Tiempo", fontsize=10)
    
    
plt.subplot(2, 2, 3) 
plt.plot(lejano)
plt.xlim([-100,105000])
plt.yticks([-500, 0, 500], [r'$-500$', r'$0$', r'$+500$'])
plt.ylim([-900,900])
plt.xticks([])
plt.title("La caminata que más se aleja", fontsize=10)

plt.subplot(2, 2, 4) 
plt.plot(cercano)
plt.xlim([-100,105000])
plt.ylim([-900,900])
plt.xticks([]), plt.yticks([])
plt.title("La caminata que menos se aleja", fontsize=10)
    
       
plt.show()


