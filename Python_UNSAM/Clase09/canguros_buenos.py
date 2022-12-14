# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:12:25 2021

@author: Silvina
"""

class Canguro():
    def __init__(self, nombre, contenido_marsupio = None):
        if contenido_marsupio is None:
            contenido_marsupio = []
            self.nombre = nombre
            self.contenido_marsupio = contenido_marsupio
    
    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)
    
    def __str__(self):
        t = [ self.nombre + ' contiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return str(t)

#%%

# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    #Uso el objeto None para denotar que hay una lista vacía porque sino
    # los objetos en el marsupio se listan cuando la función se define
    #y no cuando se llama.
    def __init__(self, nombre, contenido= None): 
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido del marsupio.
        """
        contenido = []
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return f'\n'.join(t)
        

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
    
    


