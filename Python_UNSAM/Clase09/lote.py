# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:50:34 2021

@author: Silvina Delgado
"""

#%%

class Lote:
   
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def costo(self):
         return self.cajones*self.precio

    def vender(self, cant):
        self.cajones -= cant
    
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    
      
