# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 01:26:12 2021

@author: Silvina
"""
#Ejercicio 11.14: precio_alquiler ~ superficie

import numpy as np
import matplotlib.pyplot as plt

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

x = superficie
y = alquiler

#Defino una funcion para el ajuste lineal
def ajuste_lineal_simple(x,y):
    '''funcion ajuste lineal'''
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

a, b = ajuste_lineal_simple(x, y)

grilla_x = np.linspace(start = min(superficie), stop = max(superficie))
grilla_y = grilla_x*a + b

#Error cuadratico medio
errores = alquiler - (a*superficie + b)
print(errores)
ecm = round(float((errores**2).mean()), 3)
print("ECM:",ecm )

plt.figure()
plt.text(80, 37, f'ECM = {ecm}', fontsize=10, bbox = dict(facecolor = 'None', alpha = 0.5))
g = plt.scatter(x = superficie, y = alquiler)
plt.title('Relación precio de alquiler - superficie')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('Superficie (m\u00b2)')
plt.ylabel('Alquiler ($)')

plt.show()

