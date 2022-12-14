#Silvina Delgado

#Ejercicio 1.18: Geringoso rústico
cadena = input('Insertar palabra: ')
capadepenapa = ''

for letra in cadena:    
    if letra in 'AEIOUaeiou':       #busco la vocal
        capadepenapa += letra                # capadepenapa += letra es lo mismo que capadepenapa= capadepenapa + letra agrego vocal
        capadepenapa += 'p'                  #agrego p
    
    capadepenapa += letra                    # le agrego lo del ciclo a la cadena
    
print('Su traducción al geringoso rústico es:', capadepenapa)