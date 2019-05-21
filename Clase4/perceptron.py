#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:00:28 2019

@author: derekcortez
"""
#Compuerta  AND
def funcion_activacion(x1,x2,w1,w2,b):
    operacion = (x1*w1 + x2*w2) - b
    if operacion >= 0:
        return 1
    else:
        return 0
    
entradas = [(0,0),(0,1),(1,0),(1,1)]
salidas = [0,0,0,1]

w1 = 0.5
w2 = 0.2
b = 0.24
n = 0.24

#iterador
i = 0

for x in range(0,32):
    
    if i == 4:
        i = 0
        print()
    
    x1 = entradas[i][0]
    x2 = entradas[i][1]
    D = salidas[i]
    Y = funcion_activacion(x1,x2,w1,w2,b)
    
    print("x1 = {0} x2={1} D={2} Y={3} w1={4} w2={5} b = {6}".format(x1,x2,D,Y,w1,w2,b))
    
    delta = D - Y
    d1 = n * delta * x1
    d2 = n * delta * x2
    
    w1 += d1
    w2 += d2
    
    b = b - n * delta
    
    i += 1