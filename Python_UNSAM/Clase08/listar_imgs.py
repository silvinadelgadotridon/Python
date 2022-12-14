# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:27:08 2021

@author: Silvina Delgado
"""
import os
import sys

#%%
def archivos_png(directorio):
    
    lista = [file for roots, dirs, files in os.walk(directorio) for file in files if file.endswith(".png")]
       
    return lista

#%%
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(archivos_png(sys.argv[1]))
    