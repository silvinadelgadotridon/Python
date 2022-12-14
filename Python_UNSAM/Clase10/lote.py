# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:50:34 2021

@author: Silvina Delgado
"""

#%%
import csv
import sys
import fileparse
sys.argv

#%%

class Lote:
    with open('../Data/camion.csv') as lineas:
        camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
         return self.cajones*self.precio

    def vender(self, cant):
        self.cajones -= cant
    
    def __repr__(self):
        return f'({self.nombre}, {self.cajones}, {self.precio})'
            
    def __str__(self):
        print(f'Camion con {self.lotes.__len__()} lotes:' )
        t = []
        camion = self.lotes.__iter__()
        for i in camion:
            cajones = i.cajones.__str__()
            precio = i.precio.__str__()
            t.append(f'Lote de {cajones} cajones de {i.nombre}, pagados a ${precio} cada uno')
        
        return '\n'. join(t)