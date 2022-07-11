# heedar lo que tiene un clase

class Bici:
    marca =""
    color = ""
    __encendido = False

    def __init__(self, marca ,color):
        self.marca = marca
        self.color = color


    def encender(self):
        self.__encendido = True

    def get_encendido(self):
        return self.__encendido

class BIci4x4:
    size_ruedas = 15

class BiciDeportiva(Bici, BIci4x4):
    cv = 15
    def __init__(self, marca, color ,cv , size_ruedas):
        self.marca = marca
        self.color = color
        self.cv = cv
        self.size_ruedas = size_ruedas

bici = Bici("BMW"," RDr")
print(f'Marca: {bici.marca} , Color: {bici.color}')

bici_lujo = BiciDeportiva("WW" ,"BLUE", 34 , 18) 
print(f'Marca: {bici_lujo.marca}, Color: {bici_lujo.color}, CV {bici_lujo.cv}')
print(f'Ruedas:{bici_lujo.size_ruedas}')