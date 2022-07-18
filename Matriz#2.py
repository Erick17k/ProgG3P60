from random import randint
n=int(input('Ingrese numero de filas: '))
m=int(input('Ingrese numero de columnas: '))
if n<5 or m<5:
    print('Error, debe ser mayor a 4')
elif n>30 or m>30:
    print('Error, debe ser menor a 30')
elif n!=m:
    print('Error, debe ser una matriz cuadrada')
else:
    matriz=[[int()for i in range(n)]for j in range(m)]
    matriz2=[[int()for i in range(n)]for j in range(m)]
    matriz3=[[int()for i in range(n)]for j in range(m)]
    for i in range(n):
        for j in range(m):
            matriz[i][j]=randint(50,1000)

    for i in range(n):
        for j in range(m):
            print('/',matriz[i][j],'/',end='')     
            matriz2[i][j]=matriz[i][j]
            matriz3[i][j]=matriz[i][j]
        print(' ')
    print('\n')
    
    print('Matriz original')
    for i in range(n):
        for j in range(m):
                print('/',matriz[i][j],'/',end='')
        print(' ')
    print('\n')
    
    print('Diagonal principal')
    for i in range(n):
        for j in range(m):
            if i==j:
                print('/',matriz2[i][j],'/',end='')
            else:
                print('  -  ',end='  ')
        print(' ')
    print('\n')
    
    print('Diagonal secundaria')
    for i in range(n):
        for j in range(m):
            if i+j==n-1:
                print('/',matriz3[i][j],'/',end='')
            else:
                print('  -  ',end='  ')
        print(' ')
      
            
            