# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 19:37:18 2022

@author: BRYF
"""

def readint(prompt, min, max):
    try:
        prompt=int(input("debe infresar un numero entre -10 y 10: "))
        assert prompt<-10 or prompt>10
        print("Valor fuera del rango")
        
           
    except ValueError:
         print("Error: Error en el ingreso")
v=readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
         