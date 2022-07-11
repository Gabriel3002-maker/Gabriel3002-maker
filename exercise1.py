#Presentar nombre,edad, por pantalla
import string


name = input('Ingrese su nombre: ')
edad = int(input('Ingrese su año de nacimiento: '))
año = int(input('Año Actual:'))

fecha = año -edad
print(f'Su Nombre es: {name} y su tiene {fecha}')