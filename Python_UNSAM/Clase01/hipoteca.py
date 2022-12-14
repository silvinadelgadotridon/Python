
#Ejercicio 1.11

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
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra
    
else:    
    if pago_mensual > saldo:                                      #cuando paga la hipoteca el saldo tiene que ser = 0
        pago_mensual = saldo                                      # por eso, si el pago mensual es mayor al saldo, tengo que redefinir ese pago en func del saldo que queda
        saldo = saldo - pago_mensual
        total_pagado = total_pagado + pago_mensual
   
        
    print(" Para el mes", mes, ", el total pagado es de $", round(total_pagado, 2), " y el saldo es de $", round(saldo, 2))


