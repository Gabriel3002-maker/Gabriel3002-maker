
class Auto:
    marca = ""
    color = ""
    encendido = False

    def __init__(self, marca , color ):
        self.marca = marca
        self.color = color

    coche1 = Auto("LOCO" , "NEgro")
    print(f'Marca: {coche1.marca}, Color: {coche1.color}')
    if coche1.encendido:
        print('El coche esta encendido')
    else:
        print('El coche esta apagado')

