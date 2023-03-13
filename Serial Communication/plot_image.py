import matplotlib.pyplot as plt
import os
import numpy as np

dir_path = os.getcwd()
file_name = "datos.txt"
file_path = os.path.join(dir_path, file_name)

with open(file_path, 'r') as f:
    lectura = f.readlines()
    val_y = lectura[0].split(',')
    print(type(val_y))
    for i in range(0, len(val_y)-1):
        val_y[i] = int(val_y[i])

file_name1 = "temperaturas-reales.txt"
file_path1 = os.path.join(dir_path, file_name1)
with open(file_path1, 'r') as f:
    lectura1 = f.readlines(1)[0]
    Start_Date = lectura1[:-3]
    

x = np.zeros((len(val_y)))

for i in range(0,len(val_y)):
    x[i] = i

print(x.shape)
print(len(val_y))
plt.plot(x[:-2], val_y[:-2])

# Añadir etiquetas y título
plt.xlabel('Tiempo en segundos a partir de: ' + Start_Date)
plt.ylabel('Temperatura')
plt.title('Gráfico de Temperaturas')

# Mostrar el gráfico
plt.show()
 

