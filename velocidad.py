# Autor: Patricio León Hernández, A01375610
# Descripcion: Calcula las distacnias y tiempo de un auto de acuerdo
# a la velocidad que ibas.

velocidad = int(input("¿A qué velocidad iba tu auto en km/h: "))

distancia1 = velocidad*6

distancia2 = velocidad*3.5

tiempo = 485/velocidad

print("Distancia recorrida en 6 hrs.: ", distancia1, "km")
print("Distancia recorrida en 3.5 hrs.: ", distancia2, "km")
print("Tiempo para recorrer 485 km: ", tiempo, "hrs.")