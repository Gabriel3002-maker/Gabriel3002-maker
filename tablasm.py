from unittest import result


numero = int(input("Ingrese el numero de la tabla que desea:"))
nums = range(0, 11)

for num in nums:
    result = numero * num
    print(f'{numero} x {num} = {result}')