# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:54:04 2021

@author: Silchus
"""
#Ejercicio 10.1
a = [1, 9, 4, 25, 16]
i = a.__iter__()
i.__next__()

#%%
def regresiva(n):
    while n > 0:
        yield n                 #yield: rendir/entregar
        n -= 1

for x in regresiva(10):
   print(x, end=' ')
   
#%%
def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

for line in open('../Data/camion.csv'):
        print(line, end='')

#%%
#Ejercicio 10.8
#sim_mercado tiene que estar corriendo
import os
import time

def vigilar(nombre_archivo):
    f = open('../Data/mercadolog.csv')
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        yield (f'{nombre}, {precio:.2f}, {volumen}')


def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

lines = vigilar('../Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja')
for line in naranjas:
    print(line)

#%%
def parsear_datos(lines):
    lins = csv.reader(lines)    #lee csv
    elegir_cols = ([row[index] for index in [0, 1, 2]] for row in lins)
    cambiar_tipo = ([func(val) for func, val in zip([str, float, int], row)] for row in lins)
    hace_dicts = (dict(zip(['nombre', 'precio', 'volumen'], row)) for row in lins)
    filtrar_datos = (row for row in hace_dicts if row['nombre'] in ['Mandarina','Naranja', 'Lima', 'Caqui', 'Pera'])
         
    return filtrar_datos