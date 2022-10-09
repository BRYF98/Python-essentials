# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:43:48 2022

@author: BRYF
"""

lista=[5, 6.9,"hola", True, 5]
print(type(lista))
print(len(lista))
print(lista)
print(lista[0])
print(lista[4])
print(lista[-1])
tupla=(5, 6.9,"hola", True, 5)
print(tupla[4])
print(tupla[3])

lista[0]=15
del lista[4]
print(lista)
