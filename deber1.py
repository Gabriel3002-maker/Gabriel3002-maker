#Calcular la base de un triangulo

area = int(input('Ingrese el Aréa del triangulo ')) 
altura = float(input('Ingrese la Altura '))

#Formula para calcular la base del triangulo 
# area = b * h /2  == base = 2(area)/altura

base = (2* area)/altura
print("la base del triangulo es " ,base,"cm")