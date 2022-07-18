sumainter=0 
contador1=0 
sumafuera=0 
contador2=0 
while True: 
    num1=int(input('Ingrese el primer numero: '))  
    num2=int(input('Ingrese el segundo numero: '))  
    if num1==num2:  
        print('Error los numeros no pueden ser iguales')
    else: 
        break 
if num1>num2:   
    minimo=num2 
    maximo=num1 
else: 
    minimo=num1 
    maximo=num2 
while True: 
    numero=int(input('Digite un numero: ')) 
    if numero==0: 
        break 
    if numero>minimo and numero<maximo: 
                sumainter+=numero 
    elif numero<minimo or numero>maximo: 
                sumafuera+=numero 
                contador1+=1 
    elif numero==minimo or numero==maximo: 
                contador2+=1 
print('La suma de los numero dentro del intervalo es: ',sumainter) 
print('El pomedio los numeros fuera del intervalo es: ',sumafuera/contador1) 
print('La cantidad de numeros ingresados a los limites del intervalo son: ',contador2) 
print('Fin del programa') 

        