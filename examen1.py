
#con una condicion pedir que el usuario realize operaciones
a = int(input("Ingrese un dato numerico "))
b = int(input("Ingrese un dato numerico "))


c = int(input("""Seleccione la operacion que desea realizar ingresando
        un digito numerico
        1=Suma
        2=Resta
        3=Multiplicacion
        4=Division
        """))
if c <=5:
    if c == 1:
        suma = a+b
        print("EL valor de la suma es ",suma)

    if c == 2:
        resta = a-b
        print("EL valor de la resta es ",resta)

    if c == 3:
        mult = a*b
        print("EL valor de la multiplicación es ",mult)

   
    if c == 4:
        div = a/b
        print("EL valor de la división es ",div)

else:
    print("El valor ingresado se encuentra fuera del rango 1-4")
   
   
