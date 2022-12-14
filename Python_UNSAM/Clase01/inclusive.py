#Ejercicio 1.29: Inclusivo
frase = input('Introduzca una frase en minúscula: ') 
frase_t = ''
palabras = frase.split()

for palabra in palabras:
    if palabra.endswith('os') or palabra.endswith('as'):
        lista = list(palabra)
        palabra = palabra[0:-2]+'es'

    elif palabra.endswith('o') or palabra.endswith('a'):
        lista = list(palabra)
        palabra = palabra[0:-1]+'e'
    frase_t = frase_t + ' ' + palabra

frase_t = frase_t
print('En inclusivo es: ', frase_t) 

  