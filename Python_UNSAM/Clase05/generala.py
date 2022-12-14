# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:35:53 2021

@author: Silvina Delgado
"""
#%%

import random
from collections import Counter


#%%
#Ejercicio 5.2: Generala no necesariamente servida

    
def tirar():
        tirada = []
        [tirada.append(random.randint(1,6)) for i in range(5)]
        return tirada
        
    
def es_generala(tirada):
   
    tirada = tirar ()
    
    if max(tirada) == min(tirada):
        return True
    else:
        tirada_2 = Counter(tirada).most_common()[0][0]
        tirada = [i for i in tirada if i == tirada_2]
        
        [tirada.append(random.randint(1,6)) for i in (range(5- len(tirada)))]
        
        if max(tirada) == min(tirada):
            return True    
        
        else:
            tirada_3 = Counter(tirada).most_common()[0][0]
            tirada = [i for i in tirada if i == tirada_3]
            [tirada.append(random.randint(1,6)) for i in (range(5 - len(tirada)))]
        
            if max(tirada) == min(tirada):
                return True    
            
            else: 
                return False
    
    return tirada


def prob_generala(N):
    generala = [es_generala(tirar()) for i in range (N)] 
    G = sum(generala)
    prob = G/N 
    #print(f"Tiré {N}, de las cuales {G} saqué generala")
    #print(f"La probabilidad de hacer generala en tres tiradas es de {prob}")
    return prob
 

#prob_generala(100000)

#%%



