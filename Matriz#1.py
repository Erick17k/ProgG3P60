from random import randint
x=int(input('Ingrese el numero de filas: '))
y=int(input('Ingrese el numero de columnas: '))

z =x*y
def llenar_matriz(n):
    matriz = []

    for r in range(x):
        fila = []

        for c in range(y):
            fila.append(randint(4, 30))
        matriz.append(fila)
    
    return matriz

resultado = llenar_matriz(z)
mayor = resultado[0][0]
menor = resultado[0][0]
print(resultado)
print('')
for fila in resultado:
    for valor in fila:
        if valor > mayor:
            mayor = valor
print(f"El numero mayor es: {mayor}")

