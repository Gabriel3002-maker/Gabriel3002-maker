#para calcular  el area de un poligono a = 1/2 perimetro * apotema
base = 1/2
perimetro = float(input('Ingrese el perimetro'))
apotema = float(input('Ingrese el apotema'))
apotema1 = float(input('Ingrese la raiz del apotema'))
area = base * perimetro
area1 = area * (apotema )
print(area1, '√' ,apotema1)