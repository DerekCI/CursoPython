import pandas as pd
import xlwt
import xlrd
#El dataframe lee el excel en forma similar a una talba
#Los parametros que le pasamos es nombre del excel con su extensiones
#datos a obtener
df = pd.read_excel('libro1.xlsx','hoja1')
print(df)
print('Encabezados de columnas')
print('Conocer contenido por columnas:\t')
#Escribimos tal cual el nombre de la columna de la que queremos
aux = df['NO']
print(aux[0])
#Para acceder a cada uno de los elementos de esa columna, agrega
aux = df['NO'][0]
print(aux)