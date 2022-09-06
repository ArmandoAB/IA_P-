#Del diccionario teclado2, muestra los elementos Modelo y Precio con presentación en un print().
teclado1 = {	#se crean dos siccionarios con datos estandar
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

model = teclado2['Modelo']	#se extrane el precio y el modelo del teclado2
prize = teclado2['Precio']
print('El precio del teclado ' + model + ' es de ' + prize + ' dolares.')
