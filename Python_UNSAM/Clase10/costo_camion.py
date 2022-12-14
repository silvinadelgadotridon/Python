#Silvina Delgado
#%%

import csv
import sys
import informe_final
sys.argv

#%%


def costo_camion(nombre_archivo):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()

 
# %%
#Ejercicios 7.4, 7.5

def f_principal(argv):
    camion = costo_camion(argv[0])
    return print('Costo total', camion)   
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    f_principal(sys.argv)