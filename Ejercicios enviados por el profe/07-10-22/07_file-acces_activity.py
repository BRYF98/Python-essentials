# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 18:43:30 2022

@author: BRYF
"""

file=open("devices.txt", "a")
while True:
    newItem=input("agrege un nuevo dispositivo: ")
   
    if newItem == "exit":
        print("Todo listo!")
        break
    file.write(newItem + "\n")
file.close()
    