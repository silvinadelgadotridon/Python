#%%
# Ejercicio 1.1 leer
with open('c:/Users/Usuario/Desktop/Python_UNSAM/Data/camion.csv', 'rt') as f:
        data = f.read()
print(data)
f.close()

#%% leer el archivo linea por linea con for
with open('c:/Users/Usuario/Desktop/Python_UNSAM/Data/camion.csv', 'rt') as f:
        for line in f:
            print(line, end = '')
f.close()    

#%% saltear la primera línea del archivo que contiene los nombres de las columnas con next()
f = open('c:/Users/Usuario/Desktop/Python_UNSAM/Data/camion.csv', 'rt')
headers = next(f)
print(headers)

for line in f:
    print(line, end = '')
f.close()

#%%separar los datos dentro de una línea con el método split()
f = open('c:/Users/Usuario/Desktop/Python_UNSAM/Data/camion.csv', 'rt')
headers = next(f).split(',')
print(headers)

for line in f:
    row = line.split(',')
    print(row)
f.close()

# %%
#Ejercicio 2.3
with open('c:/Users/Usuario/Desktop/Python_UNSAM/Data/precios.csv', 'rt') as f:
    fruta = []
    precio = []
    
    for line in f:
        row = line.split(',')
        
        if 'Naranja'in row[0]:
            precio = row[1]
                    
print('El precio de la naranja es: ', precio)

#%%
#Ejercicio 2.4
import gzip
with gzip.open('c:/Users/Usuario/Desktop/Python_UNSAM/Data/camion.csv.gz', 'rt') as f:
        for line in f:
            print(line, end = '')

# %%
#Ejercicio 2.5
def saludar(nombre):
    'Saluda a alguien'
    print('Hola', nombre)

# %%
#Ejercicio 2.7
def buscar_precio(fruta):
    
    with open('../Data/precios.csv') as f:
        try:                
            for line in f:
                row = line.split(',')
                if fruta in row[0]:
                    precio = row[1]
            print(f'El precio del cajón de {fruta} es {precio}')
        except:                    
            print(f'{fruta} no está en la lista')

#%%
#Ejercicio 2.8
def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad
for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')

                       

# %%
#Ejercicio 2.8 aplicado a camión

def costo_camion(nombre_archivo):
    
    with open('../Data/missing.csv', 'rt') as f:
        headers = next(f).split(',')
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

costo = costo_camion('c:/Users/Usuario/Desktop/Python_UNSAM/Data/missing.csv')
print(f'El costo de la carga de frutas es {costo}.')

#%%
#Ejercicio 2.9: Funciones de la biblioteca
import csv

def costo_camion(nombre_archivo):
    
    with open('c:/Users/Usuario/Desktop/Python_UNSAM/Data/camion.csv', 'rt') as f:
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

costo = costo_camion('../Data/camion.csv')
print(f'El costo de la carga de frutas es {costo}.')

# %%
import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
print(headers)
for row in rows:
        print(row)

f.close()
# %%
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.3),
    ('Limon', 150, 83.44)
]
# %%
#armar lista vacia
registros = []  # Empezamos con una lista vacía

# Usamos el .append() para agregar elementos
registros.append(('Pera', 100, 490.10))
registros.append(('Naranja', 50, 91.3))
#%%
with open('../Data/camion.csv', 'rt') as f:
    next(f) # Saltear el encabezado
    for line in f:
        row = line.split(',')
        registros.append((row[0], int(row[1]), float(row[2])))
# %%
