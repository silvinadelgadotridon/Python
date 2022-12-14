#%%
#Ejercicio 3.6: contar

for n in range(10):            # Contar 0 ... 9
        print(n, end=' ')

for n in range(10,0,-1):       # Contar 10 ... 1
        print(n, end=' ')

for n in range(0,10,2):        # Contar 0, 2, ... 8
        print(n, end=' ')
# %%
#Ejercicio 3.7: Más operaciones con secuencias

data = [4, 9, 1, 25, 16, 100, 49]

for x in data:      #datos iterables
        print(x)

for n, x in enumerate(data):
        print(n, x)

for n in range(len(data)):
        print(data[n])

#usá un ciclo for normal si querés iterar sobre los elementos de la variable data. Y usá enumerate() si necesitás tener el índice por algún motivo.



# %%
#Ejercicio 3.8: Un ejemplo práctico de enumerate()

def costo_camion(nombre_archivo):
    
    with open('../Data/missing.csv', 'rt') as f:
        headers = next(f).split(',')
        costo_cajon = []
        costo = 0    
        
        for n, line in enumerate(f):
            try:
                row = line.split(',')
                row[2] = row[2].rstrip()
                costo_cajon = float(row[1]) * float(row[2])     #multipicar numero de cajones por precio
                costo = costo + costo_cajon         # sumar los resultados          
            except ValueError:
                print(f'Fila {n} no se puede interpretar: {row}')    
        return costo

costo = costo_camion('../Data/missing.csv')


# %%
#Ejercicio 3.9 

import csv

def leer_camion(nombre_archivo):
    camion = {}
    lista = []           
    
    with open(nombre_archivo, 'rt', encoding= 'utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for line in f:
            try:
                row = line.split(',')
                row[2] = row[2].rstrip()
                record = dict(zip(headers, row)) 
                lista.append(record)
                camion = {}                                               
        
            except ValueError:
                print(f' No pude interpretar: {row}')     
    
    return lista




#%%
import csv

def leer_precios(nombre_archivo):
    
    with open(nombre_archivo, 'rt',encoding= 'utf8') as f:
        rows = csv.reader(f)
        precios = {}               
        
        for i, row in enumerate(rows):
            try:
                precios[row[0]] = float(row[1]) 
                #print(i+1,row)
            
            except:                    
                print(f'lista vacía {i+1}:{row}')


        return precios
        

#%%

archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'

camion = leer_camion(archivo_camion)
precios = leer_precios(archivo_precios)

ganancia = 0.0
balance = 0.0
total = 0.0
for i in camion:
    total+= int(i['cajones']) * float(i['precio'])
    if i['nombre'] in precios:
        ganancia += int(i['cajones']) * float(precios[i['nombre']])
    balance = ganancia - total

print('**********\n BALANCE\n**********\n')    
print(f"El costo del camión es {total}. Lo recaudado en la venta es {ganancia}. Por lo tanto, el balance es {round(balance, 2)}")




# %%
#Ejercicio 3.10: Invertir un diccionario

precios = {
        'Pera' : 490.1,
        'Lima' : 23.45,
        'Naranja' : 91.1,
        'Mandarina' : 34.23
    }
precios.items()
lista_precios = list(zip(precios.values(),precios.keys()))
#min(lista_precios)
#max(lista_precios)
#sorted(lista_precios)

#a = [1, 2, 3, 4]
#b = ['w', 'x', 'y', 'z']
#c = [0.2, 0.4, 0.6, 0.8]
#list(zip(a, b, c))      
#zip se puede usar para  aparear datos provenientes de diferentes lugares


# %%
#Ejercicio: Contadores

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            camion.append(record)
    return camion

camion1 = '../Data/camion.csv'
camion = leer_camion(camion1)
print(f'El camion tiene:{camion}')

camion = leer_camion(camion1)
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += int(s['cajones'])
tenencias

camion2 = leer_camion('../Data/camion2.csv')

from collections import Counter
tenencias2 = Counter()
for s in camion:
    tenencias2[s['nombre']] += int(s['cajones'])
tenencias2

combinada = tenencias + tenencias2

#%%
s = {
    'nombre': 'Naranja',
    'cajones': 100,
    'precio': 91.1
}
'{nombre:>10s} {cajones:10d} {precio:10.2f}'.format_map(s)
#format.map usa los mismo codigos de f-strings, pero toma los valores que provee el diccionario

'{nombre:>10s} {cajones:10d} {precio:10.2f}'.format(nombre='Naranja', cajones=100, precio=91.1)
#format es para darle formato a los argumentos


# %%
