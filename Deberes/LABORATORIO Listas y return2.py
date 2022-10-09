# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:36:29 2022

@author: BRYF
"""

def isYearLeap(year):
    if year %4==0 and year %100!=0:
        return True
    elif year % 100 ==0 and year % 400==0:
        return True
    else: 
        return False
def daysInMonth(year, month):
    mesesTreinta = [4,6,9,11]
    mes_entero = int(month)
    anio_entero = int(year)
    # Abril, junio, septiembre y noviembre tienen 30
    if mes_entero in mesesTreinta:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes_entero == 2:
        if isYearLeap(anio_entero):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31
    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
