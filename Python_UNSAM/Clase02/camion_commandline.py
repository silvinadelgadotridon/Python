#Silvina Delgado
# -*- coding: utf-8 -*-
import csv
import sys

def costo_camion(nombre_archivo):
    
    with open('../Data/camion.csv', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        costo_cajon = []
        costo = 0

        for line in f:
            try:
                row = line.split(',')
                costo_cajon = float(row[1]) * float(row[2])     #multipicar numero de cajones por precio
                costo = costo + costo_cajon         # sumar los resultados          
            except:
                print(f'warning')    
        return costo

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    
costo = costo_camion(nombre_archivo)
print('Costo total', costo) 