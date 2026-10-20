from funciones import mayor, menor, producto, cociente

a=int(input("Ingrese un número: "))
b=int(input("Ingrese un número: "))
if mayor(a,b) == True:
    c=producto(a,b)
    print(f"El resultado es {c}")
else:
    d=cociente(a,b)
    print(f"El resultado es {d}")