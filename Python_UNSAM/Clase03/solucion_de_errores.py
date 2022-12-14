#solucion_de_errores.py

#Ejercicios de errores en el código

#Estudiante: Silvina Delgado

#%%
#Ejercicio 3.1. Función tiene_a()

#Comentario: El error era de tipo semántico y estaba ubicado la línea 18, donde no se estaban considerando las "A" mayúsculas ni las que estaban contenidas en las palabras.
#    Lo corregí cambiando "if expresion[i] == 'a':" por "if 'a' in expresion.lower():".De este modo, se encontrarán las "A" que estén contenidas en la expresión y, las que se ingresen con mayúsculas, serán convertidas en minúsculas ser identificadas en el condicional. 
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if 'a' in expresion.lower():
            return True
        else:
            return False
    i += 1

#tiene_a('UNSAM 2020')
#tiene_a('La novela 1984 de George Orwell')
#tiene_a('abracadabra')'
#tiene_a('perro')
# %%
#Ejercicio 3.2. Función tiene_a(), nuevamente

#Comentario: Los errores eran de sintaxis y estaban ubicados en donde se definen la función y los condicionales, además de tener error en el return dentro del else.
#   Los errores se pueden solucionar escribiendo los dos puntos correspondientes a cada una de las líneas donde se requería (def, if y else), reemplazando "=" por  el operador relacional "==", "Falso" por "False" y cambiando la posición de "i+=1" abajo del else.

#tiene_a('UNSAM 2020')
#tiene_a('La novela 1984 de George Orwell')
# %%

#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de sintaxis en la prueba ya que no puedo medir la longitud del número entero 1984, sólo se puede contar los elementos de la string.

    
# %%
#Ejercicio 3.4: Alcances
#Comentario: El error es de tipo semántico y se encuentra en la linea 2 (cuando se define a c = a + b). Esto se puede solucionar haciendo que la funcion devuelva la suma de a y b con el uso de return
#Código corregido:

def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)

print(f"La suma da {a} + {b} = {c}")

# %%
#Ejercicio 3.5: Pisando memoria
#Comentario: Agregué la linea  "registro = {}" para que haga un diccionario por cada ciclo (o sea, para cada fila del archivo)
#-*-coding: utf-8 -*-
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
            registro = {}
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
# %%
