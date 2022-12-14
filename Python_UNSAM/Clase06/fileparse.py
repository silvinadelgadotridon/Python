# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:10:23 2021

@author: Silvina Delgado
"""
#%%

import csv

#%%


def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
   
    with open(nombre_archivo, encoding="utf-8") as f:
        filas = csv.reader(f)
        registros = []
        
        if has_headers:
            encabezados = next(filas)
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
            for fila in filas:
                if not fila:    
                    continue
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        
        else:
            indices = []
            for fila in filas:
                if not fila:    
                    continue
                if indices:
                    fila = [fila[index] for index in indices]
            
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]

                registro = tuple(fila)
                registros.append(registro)

    return registros

#camion = parse_csv('../Data/camion.csv', types=[str, int, float])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)

