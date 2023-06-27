import matplotlib.pyplot as plt

#gráfico en barras
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

#para gráfico de torta
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()
  

#ejecutar archivo como un script 
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10,40,800]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)







