import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leer todos los datos del archivo

data = pd.read_csv('altura-peso.csv')

#Print
print(f"Dataset: {data}")
print(f"Size: {data.shape}")

#Convertir data a numpy
data = data.to_numpy()

# Calcular media de las columnas
mean = np.mean(data, axis=0)

# Calcular matriz de covarianza utilizando la fórmula
cov_matrix = np.dot((data - mean).T, (data - mean)) / (data.shape[0] - 1)

# Imprimir matriz de covarianza
print("Matriz de covarianza:")
print(cov_matrix)

var_altura = np.sqrt(cov_matrix[(0,0)])
var_peso = np.sqrt(cov_matrix[(1,1)])
print(f"Varianza Altura:{var_altura}")
print(f"Varianza Peso:{var_peso}")

#Visualizar dataset
plt.plot(figsize=(10,7))
plt.scatter(data['Altura'], data['Peso'])
plt.show()



