colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #se crea la lista con los elementos solicitaso
print(colores)  #se muestra la lista completa
eliminados = [colores.pop(1), colores.pop(-2)]  #se eliminan los elementos azul y blanco de la lista original y se guardan en otra lista
print(colores)  #se muestra la lista modificada
print(eliminados)   #se muestra la lista creada
