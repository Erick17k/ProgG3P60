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

testYears=[1900,2000,2016,1987]
testMonths=[2,2,1,11]
testResults=[28,29,31,30]
for i in range(len(testYears)):
    yr=testYears[i]
    mo=testMonths[i]
    print(yr,mo,'->',end=' ')
    result=diasDelMes(yr,mo)
    if result==testResults[i]:
        print('OK')
    else:
        print('Failed')