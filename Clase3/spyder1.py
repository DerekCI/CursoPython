#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:30:08 2019

@author: derekcortez
"""

import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#Carcar el dataset
boston = datasets.load_boston()
print(boston)
#Revisar caracteristicas del dataset
print(boston.keys())
#print("Descripcion del dataset")
print(boston.DESCR)
#Numero de datos con los que contamos
print(boston.data.shape)#muestras, columnas
#Nombres de columnas
print(boston.feature_names)#RM numero de habitaciones
#Para el algoritmo solo necesitamos una variable, elegiremos esa
#Columna 5 (iniciando la cuenta desde 0)

#Variable X
#Cambiar de una dimension a dos
#CARGAR COLUMNA 5
x=boston.data[:,np.newaxis,5]
y= boston.target
#Vemos el grafico
plt.figure(1)
plt.scatter(x,y)
#----Separamos los datos de entrenamiento---
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2)
#Creamos un nuevo modelo de regresion lineal
lr = linear_model.LinearRegression()
#Entrenar, con los datos elegidos de la proporcion (20%) trata de hacer un modelo
lr.fit(X_train,Y_train)