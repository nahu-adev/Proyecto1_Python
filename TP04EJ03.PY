from funciones import producto, cociente

n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese otro número: "))
c=producto(n1,n2)
d=cociente(n1,n2)
print(f"El producto es {c} y la división es {d}")