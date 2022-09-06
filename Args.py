#¿Cuántos argumentos se utilizan en cada una de estas llamadas? 4, 3, 1 y 2 respectivamente
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo')
colores('lila', 'negro', 'rojo')
colores('rosa')
colores('marrón', 'naranja')

#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('verde', 'amarillo', 'morado', 'turquesa','cian','blanco')


#Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().
def suma(*args):
	suma = args[0] + args[1] + args[2] + args[3] + args[4]
	print(suma)

suma(13,43,30,3,25,41)