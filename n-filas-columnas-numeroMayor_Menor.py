
from random import randint
matriz=[]
menor=0
mayor=0
n=int(input('Ingrese el numero de filas: '))
m=int(input('Ingrese el numero de columnas: '))   
for i in range(n):
    matriz.append([0])
    for j in range(m-1):
        matriz[i].append(randint(4,30))
print(matriz)

for numero in matriz:
    for valor in numero:
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor

print(f"El numero mayor es {mayor}")
print(f"El numero menor es {menor}")