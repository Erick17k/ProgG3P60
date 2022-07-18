def bisiesto(anio):
    if anio<1582:
        return False
    elif anio%4 !=0:
        return False
    elif anio%100 !=0:
        return True
    elif anio%400 !=0:
        return False
    return True
def diasDelMes(anio,mes):
    diasMes=[31,28,31,30,31,30,31,31,30,31,30,31]
    if bisiesto(anio) and mes==2:
        return 29
    return diasMes[mes-1]
def diaDelanio(anio,mes,dia):
    if anio<1582:
        return None
    if mes>12 or mes<1:
        return None
    if dia>31 or dia<1:
        return None
    dias_totales=dia
    mes=mes-1
    while mes>0:
        dias_totales+=diasDelMes(anio, mes)
        mes-=1
    return dias_totales
print(diaDelanio(2021,1,-1))
