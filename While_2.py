x = 0
while x < 30:   #se comprueba si la variable es menor a 30
    x = x+1 #se suma 1 a la variable
    if x == 4 or x == 6 or x == 10: #si la variable vale 4, 6 o 10, se salta el ciclo
        print('se saltó la instruccion ', x)
        continue
    if x == 15: #cuando la variable vale 15 se rompe el bucle
        print('se rompio la ejecucion del bucle en el ciclo ', x)
        break
    print(x)


