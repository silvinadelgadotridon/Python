# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 16:54:55 2021

@author: Silvina Delgado
"""
#%%
import random
from tqdm import tqdm

#%%
def envidrio():
    
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    cartas_mano = random.sample(naipes,k=3) #sin reposicion
    

    if  cartas_mano[0][1] == cartas_mano[1][1]:
        while (cartas_mano[0][0] and cartas_mano[1][0]) < 10:
            tanto = cartas_mano[0][0] + cartas_mano[1][0]+ 20
            if tanto == 31:
                return True
                
        
    if  cartas_mano[0][1] == cartas_mano[2][1]:
        while (cartas_mano[0][0] and cartas_mano[2][0]) < 10:
            tanto = cartas_mano[0][0] + cartas_mano[2][0]+ 20
            if tanto == 31:
                return True
        
    if  cartas_mano[1][1] == cartas_mano[2][1]:
        while (cartas_mano[1][0] and cartas_mano[2][0]) < 10 :
            tanto = cartas_mano[1][0] + cartas_mano[2][0]+ 20
            if tanto == 31:
                return True
   
    else: 
        return False
    
N = 10000
envido_31 = [envidrio() for i in range (N)]    
G = sum(envido_31)
prob = G/N 
        
#%%
#hecho en clase


valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def dar_mano():
    return random.sample(naipes,k=3) #sin reposicion

def tengo31(cartas_mano):
    si = False
    for palo in palos:
        if (4,palo) in cartas_mano and (7,palo) in cartas_mano:
            si = True
        if (5,palo) in cartas_mano and (6,palo) in cartas_mano:
            si = True
    return si

def tengo32(cartas_mano):
    si = False
    for palo in palos:
        if (5,palo) in cartas_mano and (7,palo) in cartas_mano:
            si = True
    return si

def tengo33(cartas_mano):
    si = False
    for palo in palos:
        if (6,palo) in cartas_mano and (7,palo) in cartas_mano:
            si = True
    return si

#%%

N = 1000000
G31 = 0
G32 = 0
G33= 0

for i in tqdm(range(N)):
    cartas_mano = dar_mano()
    if tengo33(cartas_mano):
        G33 += 1
    elif tengo32(cartas_mano):
        G32 += 1
    elif tengo31(cartas_mano):
        G31 += 1

print(f"repartí {N} veces, de las culaes {G31} salió envido de 31, {G32} de 32 y {G33} de 33 ")
print(f"La probabilidad de sacar envido es {G31/N: 0.3f}, {G32/N: 0.3f}, {G33/N: 0.3f} para 31, 32 y 33, respectivamente")
