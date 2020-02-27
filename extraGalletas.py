#Autor: Patricio León
#Descripción: Teclea el número de galletas que quieres para saber la cantidad
#de ingredientes que necesitas.

galletas = int(input("¿Cuántas galletas quieres preparas?: "))
azucar = (1.5*galletas)//48
mantequilla = (1*galletas)//48
harina = (2.75*galletas)//48

print("Si quieres", galletas, """galletas tienes que tener las siguientes
cantidades de ingredientes""")
print ("Azúcar: ", azucar, "taza(s)")
print ("Mantequilla: ", mantequilla, "taza(s)")
print ("Harina: ", harina, "taza(s)")