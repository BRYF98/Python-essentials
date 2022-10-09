# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:00:05 2022

@author: BRYF
"""
numero=input("ingrese # al que debo contar: ")
numero=int(numero)
contador=1
while True:
    print(contador)
    contador+=1#contador=contador+1 es lo mismo
    if contador > numero:
        break