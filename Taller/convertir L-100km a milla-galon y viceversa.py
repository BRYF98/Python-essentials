# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:41:39 2022

@author: BRYF
"""

def l100kmtompg(lt):
    gl=lt/3.785411784 
    mi=100/1.609344
    res=mi/gl
    print(res)
def mpgtol100km(miles):
    km=miles*1.609344
    liter=3.785411784
    res2=liter/km*100
    print(res2)
print(l100kmtompg(3.9))
print(mpgtol100km(60.3))