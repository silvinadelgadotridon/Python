# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 23:38:34 2021

@author: Silvina Delgado
"""

import pandas as pd
import os

#%%
#Ejercicio 8.9: Comparando especies en parques y en veredas
directorio1 = '../Data'
archivo1 = 'arbolado-en-espacios-verdes.csv'
fname1 = os.path.join(directorio1,archivo1)
df_parques = pd.read_csv(fname1)

directorio2 = '../Data'
archivo2 = 'arbolado-publico-lineal-2017-2018.csv'
fname2 = os.path.join(directorio2,archivo2)
df_veredas = pd.read_csv(fname2)

cols1 = ['diametro','altura_tot']
cols2 = ['diametro_altura_pecho','altura_arbol']

df_tipas_parques = df_parques[df_parques['nombre_cie'] == 'Tipuana Tipu'][cols1].copy()
df_tipas_parques.insert(0,'ambiente', 'parque')
df_tipas_parques.rename(columns = {'altura_tot': 'altura_arbol', 'diametro': 'diametro_altura_pecho'}, inplace=True)


df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 'Tipuana tipu'][cols2].copy()
df_tipas_veredas.insert(0,'ambiente', 'vereda')

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
df_tipas.boxplot('altura_arbol',by = 'ambiente')



#¿Qué tendrías que cambiar para repetir el análisis para otras especies? ¿Convendría definir una función?

#Por cada especie, tendría que cambiar el código, por lo tanto convendría generarizarlo
#definiendo una función que dependa de las especies 
