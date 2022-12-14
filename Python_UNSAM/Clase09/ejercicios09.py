# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:02:42 2021

@author: Silchu
"""
class Jugador: #defino nuevo tipo de objeto usando class
#obejto yipo jugador tiene atributos x,y, salud
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100
#metodos mover y lastimar
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def lastimar(self, pts):
        self.salud -= pts

#a = Jugador(2, 3)     insancias de jugador, es decir es objeto
#de la clase jugador

#datos locales se inicializan, para cada instancia, 
#durante la ejecución del método __init__() de la clase

#%%
#Ejercicio 9.1: Objetos como estructura de datos

