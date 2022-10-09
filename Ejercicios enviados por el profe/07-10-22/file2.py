# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 18:50:31 2022

@author: Juan Carlos
"""
file = open("devices.txt", "a")
while True:
    newItem = input("Ingrese un nuevo dispositivo: ")
    if newItem == "exit":
        print("Todo Listo!")
        break
    file.write(newItem + "\n")
file.close()