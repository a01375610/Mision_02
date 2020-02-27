# Autor: Patricio León Hernández, A01375610
# Descripcion: Calcula el total de alumnos y el porcentaje de hombres y mujeres.

numeroM = int(input("Teclea el número total de mujeres inscritas: "))
numeroH = int(input("Teclea el número total de hombres inscritos: "))

total = numeroM + numeroH
porcentajeH = (numeroH/total)*100
porcentajeM = (numeroM/total)*100

print("Total de inscritos: ", total)
print("Porcentaje de mujeres: ", porcentajeM, "%")
print("Porcentaje de hombres: ", porcentajeH, "%")