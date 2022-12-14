#Ejercicio 1.1
"""
import math
print(105/60, "horas")
a=20/0.6214
print(a, "km")
print(a/1.75,"km/h" )
"""
#Ejercicio 1.2
"""
help("abs")         # abs(x, /)     Return the absolute value of the argument
help ("round")      #round(number, ndigits=None)     Round a number to a given precision in decimal digits.
"""

#Ejercicio 1.3
"""
print(12 + 20)
print(3 + 4
         + 5 + 6)

for i in range(5):
        print(i)
"""
#Ejercicio 1.4

grosor_billete = 0.11 * 0.001 # 0.11 mm en metros
altura_obelisco = 67.5         # altura en metros
num_billetes = 1
dia = 1

while num_billetes * grosor_billete <= altura_obelisco:
    print(dia, num_billetes, num_billetes * grosor_billete)
    dia = dia + 1 #reparé error: la variable "dias" no está definida, la modifiqué por "dia"
    num_billetes = num_billetes * 2

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final', num_billetes * grosor_billete)


# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca 1.8
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra = 1000

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual  
    total_pagado = total_pagado + pago_mensual 
    mes = mes + 1
    
    if mes <= 12:
        saldo = saldo-pago_extra
        total_pagado = total_pagado +pago_extra

print("Total pagado", round(total_pagado, 2), "Mes", mes)
"""

#Ejercicio 1.9 y 1.10
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual  
    total_pagado = total_pagado + pago_mensual 
    mes = mes + 1
    
    if  (mes>=pago_extra_mes_comienzo) and mes<=pago_extra_mes_fin :
        saldo = saldo-pago_extra
        total_pagado = total_pagado +pago_extra

    print("Total pagado", round(total_pagado, 2), "Mes", mes, "Saldo", saldo)
"""
#Ejercicio 1.19
'''
frutas= 'MAndarina, Kiwi,BAnana '
print(frutas.lower())
print(frutas.upper())
'''
#Ejercicio 1.20
"""
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual                                  #pago durante los 30 años
    total_pagado = total_pagado + pago_mensual 
    mes = mes + 1
    
    if  (mes>=pago_extra_mes_comienzo) and (mes<=pago_extra_mes_fin) :          # agrego los años de adelanto de hipoteca
        saldo = saldo-pago_extra
        total_pagado = total_pagado +pago_extra
else:    
     if pago_mensual > saldo:                                      #cuando paga la hipoteca el saldo tiene que ser = 0
        pago_mensual = saldo                                      # por eso, si el pago mensual es mayor al saldo, tengo que redefinir ese pago en func del saldo que queda
        saldo = saldo - pago_mensual
        total_pagado = total_pagado + pago_mensual
        
        
a= f'El total pagado es $ {round(total_pagado, 2)} y el saldo adeudado es $ {round(saldo, 2)} para el mes {mes} '
print(a)
"""
#Ejercicio 1.22
'''
frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
lista_frutas = frutas.split(',')

print(lista_frutas[0])
print(lista_frutas[1])
print(lista_frutas[2])
print(lista_frutas[-3])

lista_frutas[2] = 'Granada'
print(lista_frutas)

lista_frutas[0:3]
print(lista_frutas)

compra = []
compra.append('Pomelo')
print(compra)

lista_frutas[-2:] = compra
print(lista_frutas)

for s in lista_frutas:
        print('s =', s)
'''
#Ejercicio 1.24: Test de pertenencia
'''
frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
lista_frutas = frutas.split(',')
s= input("Insertar una fruta: ")
if s in lista_frutas:
    s = True
    print(s)
else:
    s= False
    print(s)
'''

#Ejercicio 1.25: Adjuntar, insertar y borrar elementos

'''
frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
lista_frutas = frutas.split(',')
lista_frutas.append('Mango')            #agregar mango al final de la lista
print(lista_frutas)

lista_frutas.insert(1, 'Lima')          #agregar lima en la posicion 1
print(lista_frutas)

lista_frutas.remove('Mandarina')        #eliminar mandarina
print(lista_frutas)

lista_frutas.append('Banana')           #Agregar banana al final
print(lista_frutas)

print(lista_frutas.index('Banana'))     #buscar la posición de la primera Banana

print(lista_frutas.count('Banana'))     #cuenta cantidad de veces que aparece la palabra

lista_frutas.remove('Banana')
print(lista_frutas)
'''

#Ejercicio 1.26: Sorting
'''
frutas = 'Frambuesa, Lima, Manzana, Naranja, Banana, Sandía, Pera, Mango'
lista_frutas = frutas.split(',')
lista_frutas.sort()
print(lista_frutas)
lista_frutas.sort(reverse = True)
print(lista_frutas)
'''
#Ejercicio 1.27
'''
lista_frutas = ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
a = ','.join(lista_frutas)
print(a)

b = ':'.join(lista_frutas)
print(b)
'''
#Ejercicio 1.28
lista_frutas = ['Banana', 'Mango', 'Frambuesa', 'Pera', 'Granada', 'Manzana', 'Lima']
nums = [101, 102, 103]
items = ['spam', lista_frutas, nums]
print(items)

