from random import randint
print('Ingrese numero de filas: ')
filas=int(input())
print('Ingrese el numero de columnas')
columnas=int(input())
print('\n'*2)
matriz=[[int()for i in range(filas)] for j in range(columnas)]
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]=randint(4,30)
        
        