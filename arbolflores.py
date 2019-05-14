from sklearn import tree
from sklearn.datasets import load_iris
import numpy

#Datos para clasificar 

#(features)
#Ancho #Largo (Petalos)
#ANcho #Largo (Sepalos)

iris = load_iris()

#Eliminando los 3 datos del data set 0, 50 y 100
target = numpy.delete(iris.target,[0,50,100])
data = numpy.delete(iris.data,[0,50,100])