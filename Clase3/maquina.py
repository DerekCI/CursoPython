#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:20:09 2019

@author: derekcortez
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

x=[1,5,1.5,8,1,9]
y=[1,8,1.8,8,0.6,11]

#Scatter
plt.scatter(x,y)
plt.show()

datos = np.array(list(zip(x,y)))
#Existe clase 0 y clase 1
etiquetas = [0,1,0,1,0,1]

clasificador = svm.SVC(kernel="linear",C=1.0)

#Entrenando a la maquina
clasificador.fit(datos,etiquetas)

resultado = clasificador.predict(np.array([[3,10]]))
print(resultado)



w = clasificador.coef_[0]

a= -w[0]/w[1]
b= -clasificador.intercept_[0]/w[1]

xx= np.linspace(0,10)
yy= a*xx+b

plt.plot(xx,yy,'r-',label="Hiperplano de separacion")
plt.scatter(x,y)
plt.legend()
plt.plot()
plt.show()