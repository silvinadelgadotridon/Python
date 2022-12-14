#Silvina Delgado
#%%

import informe_funciones

#%%

def costo_camion(nombre_archivo):
    costo = 0
    rows = informe_funciones.leer_camion(nombre_archivo)
    for row in rows:
        try:
            ncajones= int(row['cajones'])
            precio = float(row['precio'])  
            costo +=  ncajones* precio     
        except:
            'warning'    
    
    return costo

#costo_camion('../Data/camion.csv')





