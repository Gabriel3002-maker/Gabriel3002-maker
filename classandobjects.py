#Definicion de class
class Coche:
    marca = ""
    color = ""

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

#creamos un
coche1 = Coche("SEAT", "Negro")
coche1 = "Azul"
coche_lujo = Coche("BMW", "Plata")

print(f'Marca:{coche1.marca}, Color:{coche1.color}')
print(f'Marca:{coche_lujo.marca}, Color:{coche_lujo.color}')

