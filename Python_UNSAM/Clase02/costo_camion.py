#Silvina Delgado
#%%
#Ejercicio 2.9
import csv

def costo_camion(nombre_archivo):
    
    with open('../Data/camion.csv', 'rt') as f:
        headers = next(f).split(',')
        costo_cajon = []
        costo = 0

        for line in f:
            row = line.split(',')
            costo_cajon = float(row[1]) * float(row[2])     #multipicar numero de cajones por precio
            costo = costo + costo_cajon         # sumar los resultados
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total', costo) 

 
# %%
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

costo = costo_camion('../Data/missing.csv')
print(f'El costo de la carga de frutas es {costo}.')

# %%
