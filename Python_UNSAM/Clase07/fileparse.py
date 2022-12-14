# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:10:23 2021

@author: Silvina Delgado
"""
#%%

import csv

import gzip

#%%


def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = True):
   
    with open(lines, 'rt', encoding= 'utf8') as f:
        lines = csv.reader(f)
        registros = []

            
        if has_headers:
            encabezados = next(lines)
            
            for line in lines:
                if select:
                    indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                    encabezados = select
                else:
                    indices = []
                for n, fila in enumerate(lines):
                    if not fila:    
                        continue
                    if indices:
                        fila = [fila[index] for index in indices]
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila) ]
                            registro = dict(zip(encabezados, fila))
                            registros.append(registro)
                        except ValueError as e:
                            if silence_errors == False:
                                print(f'Fila {n+1}: No pude convertir {fila}')
                                print(f'Motivo: {e}')

        else:
            indices = []
            for fila in lines:
                if not fila:    
                    continue
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                
                registro = tuple(fila)
                registros.append(registro)
                                        
        if select:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
    
    return registros


#camion = parse_csv('../Data/camion.csv', types=[str, int, float])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)

