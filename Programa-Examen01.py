sumainter=0 #Se introdujo el primer acumulador
contador1=0 #Se introdujo el primer contador
sumafuera=0 #Se introdujo el segundo acumulador
contador2=0 #Se introdujo el segundo contador
while True: #Se propuso un bucle para el valor de verdad
    num1=int(input('Ingrese el primer numero: '))   #Definimos variable como entero
    num2=int(input('Ingrese el segundo numero: '))  #Definimos variable como entero
    if num1==num2:  #Dimos una condicion de verdad
        print('Error los numeros no pueden ser iguales') #Indicamos un error al escribir dos numero iguales
    else: #Para el valor de falso
        break #Si la condicion de falso se cumple el programa termina
if num1>num2:   #Condicion de verdad para variables num1>num2
    minimo=num2 #Reconocer minimo
    maximo=num1 #Reconocer maximo
else: #Para valor de falso
    minimo=num1 #Reconocer minimo
    maximo=num2 #Reconocer maximo
while True: #Se propuso un bucle para el valor de verdad
    numero=int(input('Digite un numero: ')) #Variable de valor entero 
    if numero==0: #Condicon de verdad para cuando numero sea cero
        break #Si el numero es cero, el programa termina
    if numero>minimo and numero<maximo: #Condicion para verdad de la parte interna del intervalo
                sumainter+=numero #En el acumulador se hace la sumainter mas el numero
    elif numero<minimo or numero>maximo: #Condicion de verdad para la parte externa del intervalo
                sumafuera+=numero #En el acumulador se hace la sumafuera mas el numero
                contador1+=1 #Se hace el contador1 mas 1 para que nos sume las veces que se digitaron numeros fuera del intervalo
    elif numero==minimo or numero==maximo: #Condicon para verdad de los limites del intervalo
                contador2+=1 #Se hace el contador2 mas 1 para que nos sume las veces que se digitaron numeros iguales a los limites del intervalo
print('La suma de los numero dentro del intervalo es: ',sumainter) #Se imprime el valor de la suma dentro del intervalo
print('El pomedio los numeros fuera del intervalo es: ',sumafuera/contador1) #Se imprime el promedio de la suma fuera del intervalo
print('La cantidad de numeros ingresados a los limites del intervalo son: ',contador2) #Se imprime la cantidad de veces de numeros ingresados iguales a los limites dle intervalo
print('Fin del programa') #Termina el programa

        