x = 0
while x < 30:
    x = x+1
    if x == 4 or x == 6 or x == 10:
        print('se saltó la instruccion ', x)
        continue
    if x == 15:
        print('se rompio la ejecucion del bucle en el ciclo ', x)
        break


