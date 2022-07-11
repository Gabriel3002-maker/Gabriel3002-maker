edad =int(input("Edad:"))
mes = int(input("Meses de Nacimiento"))
if edad>=18:
    print("Mayor de Edad")
    if mes == 1:
        print("Enero")
    
    elif mes ==2:
        print("Febrero")

else:
    print("Eres menor de edad")
    