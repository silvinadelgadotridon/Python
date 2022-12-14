#Silvina Delgado
#%%
# -*- coding: utf-8 -*-
def buscar_precio(fruta):
    
    with open('../Data/precios.csv') as f:
        contador_frutas = False         #condición inicial         
        for line in f:
            row = line.split(',')
            if fruta in row[0]:
                precio = float(row[1])
                contador_frutas = True      #encuentra la fruta
                print(f'El precio del cajón de {fruta} es {precio}')
    
    if contador_frutas == False:            # no encontró la fruta en el bucle for
        print(f'{fruta} no está en la lista')
# %%
