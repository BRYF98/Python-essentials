# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:56:37 2022

@author: BRYF
"""

def isYearLeap(year):
    if year %4==0 and year %100!=0:
        return True
    # Si es multiplo de 100 tambien tiene que ser de 400
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
    
def dayOfYear(year, month, day):
    dia_entero=int(day)
    dias_del_mes=daysInMonth(year, month)
    if dia_entero <=0 or dia_entero > dias_del_mes:
        return None
    elif month <=0 or month >=13:
        return None
    elif isYearLeap: 
        return 366
    else:
        return 365
print(dayOfYear(2000, 13, 31))
        
    
    
