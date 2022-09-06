tupla = ('naranja', 'verde', 'azul', 'negro')   #se crea una tupla con valores preferidos
color = input('Introduce un color\n')   #se lee y guarda un string

if color in tupla[0]:   #se comprueba si el string se encuentra en la tupla
    print('si hay naranja')
elif color in tupla[1]:
    print('si hay verde')
elif color in tupla[2]:
    print('si hay azul')
elif color in tupla[3]:
    print('si hay negri')
else:
    print('no hay de ese')
