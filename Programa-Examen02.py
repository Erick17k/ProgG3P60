numero=100 #Variable para que la condicion de while!=0 se cumpla
sumainter=0 #Acumulador para suma interna del intervalo
contador1=0 #Variable contador
sumafuera=0 #Acumulador para suma fuera del intervalo
contador2=-1 #Variable contador
while True: #Bucle de verdad 
    num1=int(input('Ingrese el primer numero: ')) #Variable como entero
    num2=int(input('Ingrese el segundo numero: ')) #Variable como entero
    if num1==num2: #Condicion de variables iguales entre si
        print('Error los numeor no pueden ser iguales') #Imprimir error si se digitan dos numero iguales
    else: #Para falso
        break #Si la condicon de falso se cumple el programa termina
if num1>num2: #Condicion de variables
    minimo=num2 #Reconcer variable minima
    maximo=num1 #Reconcer variable maxima
else: #Para falso
    minimo=num1 #Reconcer variable minima
    maximo=num2 #Reconcer variable maxima
while numero!=0: #Condicion para el bucle
    numero=int(input('Digite un numero: ')) #Variable como entera
    if numero>minimo and numero<maximo: #Condicon de verdad para la parte interna del intervalo
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
