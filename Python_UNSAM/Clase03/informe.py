# %%
# Silvina Delgado
#Ejercicio 3.9 
import csv

def costo_camion(nombre_archivo):
    
    with open('../Data/camion.csv', 'rt', encoding= 'utf8') as f:
        headers = next(f).split(',')
        costo_cajon = []
        costo = 0

        for line in f:
            row = line.split(',')
            costo_cajon = float(row[1]) * float(row[2])     #multipicar numero de cajones por precio
            costo = costo + costo_cajon         # sumar los resultados
    return costo

costo = costo_camion('../Data/camion.csv')



def leer_camion(nombre_archivo):
    camion = {}
    lista = []           
    
    with open('../Data/camion.csv', 'rt', encoding= 'utf8') as f:
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

lista = leer_camion('../Data/camion.csv') 


def leer_precios(nombre_archivo):
    
    with open('../Data/precios.csv', 'rt',encoding= 'utf8') as f:
        rows = csv.reader(f)
        precios = {}               
        
        for i, row in enumerate(rows):
            try:
                precios[row[0]] = float(row[1]) 
                #print(i+1,row)
            
            except:                    
                print(f'lista vacía {i+1}:{row}')

        return precios

precios = leer_precios('../Data/precios.csv')       




ganancia = 0.0
balance = 0.0
total = 0.0
for i in lista:
    total+= int(i['cajones']) * float(i['precio'])
    if i['nombre'] in precios:
        ganancia += int(i['cajones']) * float(precios[i['nombre']])
    balance = ganancia - total

print('**********\n BALANCE\n**********\n')    
print(f"El costo del camión es {total}. Lo recaudado en la venta es {ganancia}. Por lo tanto, el balance es {round(balance, 2)}")

# %%
