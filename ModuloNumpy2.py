#Importar el módulo
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from sympy import *
from mpl_toolkits.mplot3d import axes3d
"""
#			ARRAY
#Declarar un vector
lista2=[1,2,3]
a = np.array([7,8,9])
a2 = np.array(lista2)
#Declarar una matriz
b = np.array([[1,1,1],[2,2,2],[3,3,3]])
print(a)
print(b)
#Operaciones entre vectores o matrices
#Suma
print(a+1)
#Producto punto
print(a.dot(a2))
#Multiplicacion de matrices
m1 = np.array([[5,5,5],[6,6,6],[7,7,7]])
m2 = np.array([[4],[3],[5]])
m1.dot(m2)
#Dudas de dimension
print(m1.shape[0])
#Arrays predeterminados
b= np.zeros((2,4))
b= np.ones(5)
b= np.arange(10,30,5)
b= np.linspace(0,2,9)
b= np.eye(1) #identidad

#			MATRIZ
a = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
#Transpuesta
print(a.T)
#Hermitica
print(a.H)
#Inversa
print(a.I)
#Diagonal principal
print(np.diag(a))
m2 = np.matrix([[5,5,5],[6,6,6]])
m1 = np.matrix([[4,4],[3,3],[2,2]])
print(m2*m1)

#Variables simbolicas
x = Symbol('x')
x,y,z = symbols('x,y,z')
print(x+y+z)

print((x+y+z).subs(a,1))
#Varias sustiticiones
expr = x*2 + 5*y-z
d=expr.subs([(x,2),(y,4),(z,0)])
print(d)
#Solucion de ecuaciones
print(solve(expr,z))
#Calculo integral
print(integrate(x**4+y,x))
#Series de McLaurin
print(cos(x).series(x,0,10))
b= Poly(x**2-3*x+2)
#Derivada
x = diff((pow(x,2)+(pow(2*x,3))+2),x)
#Limites
limit(cos(x)/x,x,0)

x = sp.linspace(0,10,100)
y = sp.cos(x)
plt.figure(1)
plt.plot(x,y,'b')
plt.title("Mi grafica")
plt.ylabel("Ordenadas")
plt.xlabel("Abcisas")
plt.show()
"""
fig = plt.figure()
ax1 = fig.add_subplot(111,projection='3d')

x= np.array([[1,2,3,4,5,6,7,8,9]])
y= np.array([[1,2,3,4,5,6,7,8,9]])
z= np.array([[9,8,7,6,5,4,3,2,1]])

ax1.plot_wireframe(x,y,z)
ax1.set_title("Figura")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")
plt.show()