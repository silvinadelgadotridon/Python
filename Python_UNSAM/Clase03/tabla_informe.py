#%%
#Silvina Delgado
#Ejercicios 3.13-3.16
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
                camion['nombre'] = row[0]
                camion['cajones'] = int(row[1])
                camion['precio'] = float(row[2])
                lista.append(camion)
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
import csv

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


#%%
import csv

def hacer_informe(camion, precios):
        lista = []
        tupla = []
        headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
        for i in camion:
                tupla.append(i['nombre'])
                tupla.append(int(i['cajones']))
                tupla.append(float(i['precio']))
                cambio = precios[i['nombre']]- float(i['precio'])
                tupla.append(cambio)
                lista.append(tupla)
                tupla = []
        
        
        for i in headers:
            
            print(f'{i:>10s}', end = ' ' )
        print('\n')
            
        print(f'---------- ---------- ---------- ----------', end = '\n')
        for nombre, cajones, precio, cambio in lista:
                precio_1 = f'${round(precio, 2)}'
                print(f'{nombre:>10s} {cajones:>10d} {precio_1:>10s} {cambio:>10.2f}')
        return lista

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)

# %%
