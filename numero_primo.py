#numero primo cunado es divisible for 1 and 0
n = int(input('Ingrese un numero:'))
esprimo = True
for i in range (2 , n):
    if ( n%i==0):
        esprimo = False
        break 
if esprimo:
        print("Es un numero primo")
else:
        print('El valor ingresado no es un numero primo')