palabras=[]

cantidad = int(input("¿Cuántas palabras desea ingresar?: "))
for i in range (cantidad):
    dato = str(input(f"Ingrese la palabra {i+1}: "))
    if len(dato)>5:
        palabras.append(dato)

print(palabras)