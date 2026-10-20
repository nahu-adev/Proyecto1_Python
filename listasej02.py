numeros = []

cantidad = int(input("¿Cuántos números desea ingresar?: "))
for i in range (cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
    numeros.sort()
    numeros.reverse()

print(numeros)