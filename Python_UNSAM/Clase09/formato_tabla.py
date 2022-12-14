# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:53:55 2021

@author: Silvina 
"""
class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
#%%

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

#%%
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

#%%
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print('<tr>', end='')
        for i in headers:
            print(f'<th>{i}</th>', end='')
        print('<tr>')

    def fila(self, data_fila):
        print('<tr>', end='')
        for j in data_fila:
           print(f'<td>{j}</td>', end='')
        print('<tr>')

#%%
def crear_formateador(fmt):
    
    if fmt == 'txt':
        formateador = FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = FormatoTablaCSV()
    elif fmt == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    return formateador
    
#%%
def imprimir_tabla(archivo, columnas, formateador):
    '''
    A partir de lista de objetos, imprime tabla 
    a partir de lista de atributos especificados por usuarix
    '''
    for colname in columnas:       
        print(colname, '', getattr(formateador.fila(archivo), colname))
    