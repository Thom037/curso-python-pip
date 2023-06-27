#archivos CSV, más comunes, información en filas y columnas
#procesas y analizar
#leer archivo y convertirlo en un array de diccionarios

import csv
#función para leer un archivo CSV, va a recibir la dirección del archivo

def read_csv(path):
  with open(path,'r') as csvfile: #función para abrir el archivo en modo lectura únicamente 
    reader = csv.reader(csvfile, delimiter = ',') #datos separados por comas
    #este reader es un iterable, su primer valor es el nombre de las filas, todo se recorre por filas 
    header = next(reader)
    data = []
    
    for row in reader:
      iterable = zip(header,row) 
      country_dict = {key:value for key, value in iterable}
      data.append(country_dict)
    return data
      

      

#ejecutar archivo como un script
if __name__ == '__main__':
  data = read_csv('./app/data.csv') #para correrlo desde terminal
  print(data[0])

#cada columna viene como array
#necesito un array formato diccionario, la llave va a a ser el nombre de la columna

      
