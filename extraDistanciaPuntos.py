# Autor: Patricio León Hernández, A01375610
# Descripcion: Calcula la distancia entre dos puntos.

import math

punto1x = int(input("Teclea las cordenadas de x1: "))
punto1y = int(input("Teclea las cordenadas de y1: "))
punto2x = int(input("Teclea las cordenadas de x2: "))
punto2y = int(input("Teclea las cordenadas de y2: "))

distancia = math.sqrt((punto1x - punto1y)**2 + (punto2x - punto2y)**2)

print ("La ditancia de la línea es: ", distancia)