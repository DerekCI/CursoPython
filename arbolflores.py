from sklearn import tree
from sklearn.datasets import load_iris
import numpy

#Datos para clasificar 

#(features)
#Ancho #Largo (Petalos)
#ANcho #Largo (Sepalos)

iris = load_iris()

prueba_target = iris.target[50]
prueba_data = iris.data[50]

#Eliminando los 3 datos del data set 0, 50 y 100
target = numpy.delete(iris.target,[0,50,100])
data = numpy.delete(iris.data,[0,50,100],axis=0) #Axis = 0 son renglones


clasificador = tree.DecisionTreeClassifier()