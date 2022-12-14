# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:31:29 2021

@author: Usuario
"""
#MÓDULO DATETIME

import datetime

#Obtener fecha y hora actuales

fecha_hora = datetime.datetime.now()
print(fecha_hora)


#Obtener fecha actual
fecha = datetime.date.today()
print(fecha)

#%%
#CLASE DATETIME.DATE

#Un objeto para represnetar una fecha
from datetime import date
d = date(2019, 4, 13)
print(d)

#%%
#Obtener la fecha a partir de un timestamp
#se toma como medida de tiempo el número de segundos 
#transcurridos desde el primero de enero de 1970 a las 0 horas UTC 
#hasta el momento a representar
timestamp = date.fromtimestamp(1326244364)
print('Fecha =', timestamp)

#%%
#Obtener el año, el mes y el día por separado
from datetime import date

hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes

#%%
#Representar la hora con un objeto time
from datetime import time
a = time()       # time(hour = 0, minute = 0, second = 0)
print('a =', a)

#%%
#Obtener horas, minutos, segundos y micro-segundos
from datetime import time

a = time(11, 34, 56)

print('hour =', a.hour) #extraigo atributos
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)

#%%
#CLASE DATETIME.DATETIME

#Objeto datetime

from datetime import datetime

# datetime(year, month, day)
a = datetime(2020, 4, 21)
print(a)

#%%
#Obtener año, mes, día, hora, minutos, timestamp de un datetime
from datetime import datetime

a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())


#%%
#CLASE DATETIME.DELTA
#Diferencia entre fechas y horarios
from datetime import datetime, date

t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)
t3 = t1 - t2
print(t3)

t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print(t6)
print('tipo de t3 =', type(t3))
print('tipo de t6 =', type(t6))

#%%
#Diferencia entre objetos timedelta
from datetime import timedelta
t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2 # t3 tambien es <class 'datetime.timedelta'>

#Duración en segundos
t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundos totales =', t.total_seconds())

#%%
#Ejercicio 8.2: Cuánto falta
from datetime import datetime

fecha_hoy= datetime.today()

#Convierto string en objeto datetime 
fecha_prim = "21/09/2022"
prim = datetime.strptime(fecha_prim, '%d/%m/%Y')
#Obtengo fecha y hora actual
dias_prim = prim - fecha_hoy


print("Faltan", dias_prim.days, "días para la primavera")

#%%
#Ejercicio 8.3: Fecha de reincorporación
from datetime import date, timedelta

d = date(year = 2020, month= 9, day = 26)
d2 = timedelta(days = 200) 
d3 = d + d2
print("La reincorporación será el día", d3) 

#%%
#Ejercicio 8.4: Días hábiles
def dias_habiles(inicio, fin, feriados):


#%%
#Lectura de datos

import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

#%%
#veo las primeras 3 lineas
df.head(3)

#veo las ultimas tres 
df.tail(3) 

#me devuelve un indice con los nombres de las columnas del DataFrame
df.columns 

#muestra el indice
df.index 

#Puedo elegir algunas columnas para inspeccionar datos levantados
df[['altura_tot', 'diametro', 'inclinacio']].describe() 

#seleccion de frgmentos de tabla. Elijo nombres únicos
df['nombre_cie'].unique()  
  
#Cuántos se llaman Ombú
df['nombre_com'] == 'Ombú'

#Podemos sumar los True de esta serie para contar la cantidad de Ombús
(df['nombre_com'] == 'Ombú').sum()

#Si queremos hacer lo mismo para otras especies
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.head(10) #para 10 especies en orden decreciente

#booleanas para seleccionar filas dle DataFrame
df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]

#Si quiero modificar df_jacarandas, es conveniente crear una copia
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()

#Scatterplots
df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')

#uso seaborn para visualizar datos, es mas piola que pandas
import seaborn as sns

sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

#Filtros por índice y por posición
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.index
#cant_ejemplares es una serie que tiene los nombres de 
#las especies como índice y sus respectivas cantidades como dato asociado.

#%%
#Ejercicio 8.7: Lectura y selección, Ejercicio 8.8: Boxplots

import pandas as pd
import os
import seaborn as sns

#leo datos
directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]
cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()
print(cant_ejemplares.head(10)) #para 10 especies en orden decreciente

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
print(df_lineal_seleccion)

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')  

#Ejemplo de pairplot
#Gráfico tiene una fila (y columna) por cada variable numérica en el DataFrame pasado como data
#hue selecciona la variable categórica a usar para distinguir subgrupos y asociarles colores
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')  
