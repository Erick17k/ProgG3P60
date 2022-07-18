def validar(nombre,edad,cedula,email):
    m=''
    t=1
    e=['!','¡','#','%','^','&','*','=','(',')','?','¿','-','_','+','`','|','~',',','<','>',',','|']
    
    if len(cedula) < 10:
        m+='La cedula es menor a 10 digitos'
        t=0
        
    elif len(cedula) >= 11:
        m+='La cedula es mayor a 10 digitos'
        t=0
        
    elif edad < 12:
        m+='La edad ingresada es menor a 12'
        t=0
        
    elif edad > 90:
        m+='La edad ingresada es mayor a 90'
        t=0
        
    elif not email.endswith('@edu.ec'):
        m+='El correo ingresado no termina en @edu.ec'
        t=0
        
    elif '@' in email[0]:
        m+='El correo ingresado inicia con arroba'
        t=0
        
    elif email.count('@') > 1:
        m+='El correo ingresado tiene mas de un arroba'
        t=0
        
    elif ' ' in email:
        m+='El correo ingresado tiene espacios en blanco'
        t=0
        
    elif '.' in email[0]:
        m+='El correo ingresado inicia con un punto'
        t=0
        
    elif len(nombre) < 3:
        m+='El nombre ingresado es menor a 3 digitos'
        t=0
        
    elif ' ' not in nombre:
        m+='Debe ingresar dos nombres'
        t=0
        
    for i in nombre:
        for j in e:
            if i == j:
                m+='El nombre ingresado tiene caracteres especiales'
                t=0
    
    for i in email:
        for j in e:
            if i == j:
                m+='El email ingresado tiene caracteres especiales'
                t=0
                
    if t == 0:
        return(False)
    else:
        return(True)
    
print(validar("Alison Porozo",19,"1725643786","aporozoa@edu.ec"))
print(validar("Julian Proaño",16,"1231232","$#$@ @edu.ec"))
print(validar("@#$@",20,"3465343355","thalia@edu.ec"))
print(validar("Erick Gómez",95,"7453425455","erick@edu.ec"))
print(validar("Thalia Vizuete",88,"2445445","$#$@ @edu.ec"))
print(validar("Santiago Perez",40,"1262736272","santiago@edu.com"))
print(validar("Alison Porozo",29,"172","aporozoa@edu.ec"))
