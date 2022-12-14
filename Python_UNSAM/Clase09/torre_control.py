# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:11:16 2021

@author: Silvina
"""
#torre_control.py

class TorreDeControl():

    def __init__(self):
        '''
        Crea dos lista vacias:
        una para los despegues 
        y otra con prioridad (aviones que esperan para aterrizar)
        '''
        self.items = []
        self.items_con_prioridad = []

    def nuevo_arribo(self, x):
        '''
        Encola elemento x
        '''
        self.items_con_prioridad.append(x)

    def nueva_partida(self, x):
        '''
        Despega un avión si no hay ninguno para aterrizar
        '''
        self.items.append(x)

    def ver_estado(self):
        '''
        Devuelve aviones esperando aterrizar(prioridad) y despegar
        '''
        print (f'Vuelos esperando para aterrizar: {self.items_con_prioridad}')
        print (f'Vuelos esperando para despegar: {self.items}')
    
    def asignar_pista(self):
        if len(self.items_con_prioridad):
            vuelo = self.items_con_prioridad.pop(0)
            print(f'El vuelo {vuelo} aterrizó con éxito')
        else:
            print('No hay vuelos en espera')
            

#%%
#import torre_control

#torre = torre_control.TorreDeControl()
#torre.nueva_partida('KLM1267')
#torre.nuevo_arribo('AR32')
#torre.ver_estado()
#torre.asignar_pista()
#torre.asignar_pista()
#torre.asignar_pista()
#torre.asignar_pista()


