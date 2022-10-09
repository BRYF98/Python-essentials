# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 19:29:28 2022

@author: BRYF
"""

dict1={"R1":"10.0.0.1","R2":"10.0.0.2", 5100: "Juan", "Email":"pappp@gmail.com"}
print(dict1)
print(type(dict1))
print(len(dict1))
print(dict1["R1"])
print(dict1[5100])
print(dict1["Email"])
dict1["S1"]="11.0.0.1"
dict1[5]=18
print("R3"in dict1)