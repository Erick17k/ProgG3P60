from random import randrange
from time import sleep

n=int(input('Ingrese el tamaño del vector: '))
vec=[]
for i in range(n):
	vec.append(randrange(50,100))

for j in range(n):
	print(f'El valor en la posición {j+1} es {vec[j]}')
	sleep(1)

for t in range(len(vec)-1,0,-1):
        for g in range(t):
            if vec[g]>vec[g+1]:
                aux=vec[g]
                vec[g]=vec[g+1]
                vec[g+1]=aux

for r in range(n):
	print(f'El vector ordenado en la posición {r+1} es {vec[r]}')
	sleep(1)
    