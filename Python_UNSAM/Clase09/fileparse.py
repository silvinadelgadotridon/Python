# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 23:10:23 2021

@author: Silvina Delgado
"""
#%%

import csv
import gzip


def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    filas = csv.reader(nombre_archivo)
        # Lee los encabezados o deja select
    if has_headers:
            encabezados = next(filas)
            if select:
                 indices = [encabezados .index(nombre_columna) for nombre_columna in select]
                 encabezados  = select
            else:
                indices = []
        
            registros = []
            for num, fila in enumerate(filas):
                
                    if not fila:    # Saltea filas sin datos
                        continue
                    if indices:
                        fila = [fila[index] for index in indices]
                    if types:
                        try:
                            fila = [func(val) for func, val in zip(types, fila)]
                            registro = dict(zip(encabezados , fila))
                            registros.append(registro)
                        except ValueError as e:
                            if silence_errors:
                                print(f'Fila {num+1}: No pude convertir {fila}')
                                print(f'Fila {num+1}: Motivo: {e}')
                                  
    else:
        registros = []
        indices = []
        for fila in filas:
                if not fila:    # Saltea filas sin datos
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

