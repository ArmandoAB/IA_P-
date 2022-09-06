#Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.
edad = int(input('¿Cuál es tu edad?\n'))	#recibe un valor de entrada tipo int y lo guarda
if edad <= 0:	#compara si ese valor es menor a 0
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad < 18:	#compara si ese valor es mayor o igual a 1 y menor a 18
	print('Eres menor de edad.')
elif edad >= 18 and edad < 45:	#compara si el valor es mayor o gual a 18 y menor a 45
	print('Eres un adulto.')
elif edad < 100:	#compara si el valor es menor a 100
	print('Eres un adulto mayor')
elif edad >= 100 and edad <= 120:	#compara si el valor es mayor o igual a 100 y menor o igual a 120
	print('Puede que estes en un libro de records')
else:
	print('Edad no válida.')
