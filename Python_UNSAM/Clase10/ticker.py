# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:41:32 2021

@author: Silvina
"""
# ticker.py

from vigilante import vigilar
import csv
from formato_tabla import crear_formateador
from informe_final import leer_camion


def parsear_datos(lines):
    lins = csv.reader(lines)    #lee csv
    elegir_cols = ([row[index] for index in [0, 1, 2]] for row in lins)
    cambiar_tipo = ([func(val) for func, val in zip([str, float, int], row)] for row in lins)
    hace_dicts = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in lins)
    filtrar_datos = (row for row in hace_dicts if row['nombre'] in ['Mandarina','Naranja', 'Lima', 'Caqui', 'Durazno'])
         
    return filtrar_datos
 

def ticker(camion_file, log_file, fmt):
    camion = leer_camion(camion_file)
    lines = vigilar(log_file)   
    
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    
    for line in lines:
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
    
        if nombre in camion:
            rows = formateador.fila(fields)
                   
        
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
        