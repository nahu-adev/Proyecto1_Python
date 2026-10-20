nombres = []

cantidad = int(input("¿Cuántos nombres desea ingresar?: "))
for i in range (cantidad):
    nombre = str(input(f"Ingrese el nombre {i+1}: "))
    nombres.append(nombre)
print(nombres)