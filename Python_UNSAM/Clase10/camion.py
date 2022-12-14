# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:49:43 2021

@author: Silvina
"""

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()    #clase Camion iterable
    
    def __len__(self):
        return self.lotes.__len__()    #clase Camion iterable

    def __getitem__(self,a):
        return self.lotes[a]

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
    
    def __repr__(self):
        return f'Camion({self.lotes})'
    
    def __str__(self):
        print(f'Camion con {self.lotes.__len__()} lotes:' )
        t = []
        camion = self.lotes.__iter__()
        for i in camion:
            cajones = i.cajones.__str__()
            precio = i.precio.__str__()
            t.append(f'Lote de {cajones} cajones de {i.nombre}, pagados a ${precio} cada uno')
        
        return '\n'. join(t)

