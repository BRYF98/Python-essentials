# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:58:51 2022

@author: BRYF
"""

while True:
        x=input("Enter a number to count to: ")
        if x=='q' or x=='quit':
            break
        x=int(x)
        y=1
        while True:
            print(y)
            y=y+1
            if y>x:
                break
                        

