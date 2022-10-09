# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:17:04 2022

@author: BRYF
"""

acl=int(input("Ingrese el número de ACL: "))
if acl >=1 and acl<=99:
    print("Es una ACL de tipo estandar")
elif acl >=100 and acl<=199:
    print("Es una ACL de estendida")
else: 
    print("No es un ACL")