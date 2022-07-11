#no se puede accder desde fuera a una clase
class Persona:
    Genero  = ""
    Edad = ""
    despierto= False

    def __init__(self, Genero , Edad) :
        self.Genero = Genero
        self.Edad = Edad

    #funcion
    def vivo(self):
        self.__despierto = True

    def get_vivo(self):
        return self.__despierto

hombre1 = Persona("Hombre" , "loco")
hombre1.vivo()
#hombre1.vivo = True

print(f'Genero:{hombre1.Genero}, Edad:{hombre1.Edad}')
print(f' Vivo:{hombre1.despierto}')
