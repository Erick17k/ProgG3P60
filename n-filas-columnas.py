from random import randint
matriz=[]
n=int(input('Ingrese el numero de filas: '))
m=int(input('Ingrese el numero de columnas: '))   
for i in range(n):
    matriz.append([0])
    for j in range(m-1):
        matriz[i].append(randint(4,30))
print(matriz)
