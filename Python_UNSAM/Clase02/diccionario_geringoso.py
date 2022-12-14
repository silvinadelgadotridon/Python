#Silvina Delgado
#%%
#Ejercicio 2.14

def diccionario_geringoso(nombre):
    nompobrepe = ''
    lista = []                              #Empiezo con la lista vacía

    for k in nombre:
        for letra in k:    
            if letra in 'AEIOUaeiou':       #busco la vocal
                nompobrepe += letra                
                nompobrepe += 'p' + letra   #agrego p+vocal               
            else:
                nompobrepe += letra         #si no es vocal, la dejo en la cadena
        lista.append(nompobrepe)            #agrego elemento a la lista
        nompobrepe = ''                     #con esto corto en cada item y no lo acumula

    d = dict(zip(nombre, lista))            #creo un diccionario que tenga el nombre y lo que generé con los ciclos 
    return d                                #zip() es para hacer tuplas de dos elementos(nombre y la lista que generé con palabras en geringoso) en la lista


frutas = ['banana', 'manzana', 'mandarina']
print(diccionario_geringoso(frutas))
# %%
