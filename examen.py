#Dado los numeros enteros del 1 al 7 escribir el dia de la semana
#al que corresponda teniendo encunta que el primer dia de la semana es lunes
numero =int(input("Ingrese un valor en el ramgo del 1-7 "))
if (numero >=8):
    if numero == 1 :
        print('El  dia es Lunes')
    if numero == 2 :
        print('El  dia es Martes')
    if numero == 3 :
        print('El  dia es Miercoles')
    if numero == 4 :
        print('El  dia es Jueves')
    if numero == 5 :
        print('El  dia es Viernes')
    if numero == 6 :
        print('El  dia es Sabado')
    if numero == 7 :
        print('El  dia es Domingo')

else:
    print('El valor es incorrecto')
