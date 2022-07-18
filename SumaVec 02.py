vector1=[1,2,3,4,5]
vector2=[1,2,3,4,5]
vector3=[0]*5

#Suma

for i in range(0,5):
    vector3[i]=vector1[i]+vector2[i]
    
for i in range(0,5):
    print(vector3[i],end=' ')
print('\n')

#Resta

for i in range(0,5):
    vector3[i]=vector1[i]-vector2[i]
    
for i in range(0,5):
    print(vector3[i],end=' ')
print('\n')

#Division

for i in range(0,5):
    vector3[i]=vector1[i]/vector2[i]
    
for i in range(0,5):
    print(vector3[i],end=' ')
print('\n')

#Multiplicacion

for i in range(0,5):
    vector3[i]=vector1[i]*vector2[i]
    
for i in range(0,5):
    print(vector3[i],end=' ')
print('\n')
 
#Exponencial

for i in range(0,5):
    vector3[i]=vector1[i]**vector2[i]
    
for i in range(0,5):
    print(vector3[i],end=' ')
print('\n')
