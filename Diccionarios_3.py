#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1	#se borra teclado1
del teclado2['Categoría']	#se borra categoría de teclado2
del teclado2['Precio']	#se borra precio de teclado2
print(teclado2)	#se imprime la clave modelo
