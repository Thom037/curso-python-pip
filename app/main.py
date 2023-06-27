#palabra clave para llamar módulos
#cuando está dentro de una carpeta para correr en la shell se usa es slash carpeta/archivo.py
#Para aceder al contenido del módulo se usa el nombre del módulo PUNTO
#Un módulo puede contener clases, funciones, variables, etc
#Usar un módulo en otro archivo = modularizar

#Colocar nombres a los módulos intuitivos

#Si yo quiero acceder a este variable desde otro archivo, la saco de la función principal

#Para controlar la ejecución si se usar como módulo en otro archivo, se coloca todo en una función RUN

#Proyeco de obtener los valores CSV, escoger un país y realizar la gráfica de la población a través de los años

import utils
import read_csv
import charts

#solución para mostrar la cantidad de población de acuerdo a su ubicación

def run():
  data = read_csv.read_csv('data.csv')  
  data = list(filter(lambda item:item['Continent']=='South America', data))
  
  countries = list(map(lambda x : x['Country/Territory'], data)) 
  percentages = list(map(lambda x : x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  

  country = input('Type Country => ')

  result =  utils.population_by_country(data, country)

  if len(result) > 0: #si se encontró ese país
    country = result[0]
    labels, values = utils.get_population(country)
    #hasta acá ya tendríamos la información en formato de diccionario 
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  
  
  
if __name__ == '__main__':
  run()


  
