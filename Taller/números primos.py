# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:53:19 2022

@author: BRYF
"""

def isPrime(num):
    if num<=1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i==0: # % es el residuo
                return False
        return True
for i in range (1,20):
    
	if isPrime(i + 1):
			print(i + 1, end=" ") #end=" " es para imprimir de forma horizontal

    