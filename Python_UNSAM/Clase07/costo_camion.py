#Silvina Delgado
#%%

import csv
import sys
import informe_final
sys.argv

#%%


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

 
# %%
#Ejercicios 7.4, 7.5

def f_principal(argv):
    camion = costo_camion(argv[0])
    return print('Costo total', camion)   
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    f_principal(sys.argv)