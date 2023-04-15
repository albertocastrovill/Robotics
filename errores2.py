import numpy as np
import matplotlib.pyplot as plt

# Función de matriz de transformación
def transf_matrix(theta, a):
    R = np.array([[np.cos(theta), -np.sin(theta), -a*np.cos(theta)],
                  [np.sin(theta), np.cos(theta), -a*np.sin(theta)],
                  [0, 0, 1]])
    return R

# Función de cinemática directa
def forward_kinematics(theta1, theta2, d1, d2):
    # Matriz de transformación del primer eslabón
    T1 = transf_matrix(theta1, d1)
    
    # Matriz de transformación del segundo eslabón
    T2 = transf_matrix(theta2, d2)
    
    # Matriz de transformación total del brazo robótico
    T = T1 @ T2
    
    # Coordenadas del extremo del brazo robótico
    x = T[0, 2]
    y = T[1, 2]
    
    return x, y

# Generar 100 muestras aleatorias con errores
x_error_samples = []
y_error_samples = []

for i in range(100):
    # Generar ángulos y distancias aleatorias para los dos eslabones
    theta1 = np.random.uniform(0, np.pi)
    theta2 = np.random.uniform(0, np.pi)
    d1 = np.random.uniform(0, 2)
    d2 = np.random.uniform(0, 2)
    
    # Calcular las coordenadas del extremo del brazo robótico
    x, y = forward_kinematics(theta1, theta2, d1, d2)
    
    # Agregar errores aleatorios a las coordenadas
    x_error = x + np.random.normal(0, 0.1)
    y_error = y + np.random.normal(0, 0.1)
    
    # Agregar las coordenadas con errores a la lista de muestras
    x_error_samples.append(x_error)
    y_error_samples.append(y_error)

# Graficar las muestras con errores
plt.scatter(x_error_samples, y_error_samples)
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Muestras con errores de brazo robótico')
plt.show()
