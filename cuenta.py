# Autor: Patricio León Hernández, A01375610
# Descripcion: Calcula la propina y el IVA de tu cuenta de acuerdo
# a el costo de tu comida.

costo = int(input("Teclea el costo de tu comida: "))
propina = 0.13*costo
IVA = 0.16*costo
total = costo+propina+IVA

print("Costo de su comida: $", costo)
print("Propina: $", propina)
print("IVA: $", IVA)
print("Total a pagar: $", total)