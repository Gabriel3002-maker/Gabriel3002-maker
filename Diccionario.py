from unicodedata import name


data = {'name':'Gabriel', 'lastname':'Vargas' , 'Age':18}
print(data['name'])

#print(f'Mi nombre es {data["lastname"]}')

#Añadir valor a diccionario
data['city']='Loja'
print(data)

#Eliminar valor a diccionario
del data['Age']
print(data)

#Cuantas claves tenemos
print(len(data))