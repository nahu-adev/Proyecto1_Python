from funciones import promedio

cantidad=int(input("¿Cuántos números ingresara para promediar?:"))

numeros = []

for x in range(cantidad):
    num=int(input(f"Ingrese el número {x+1}: "))
    numeros.append(num)

res = promedio(numeros)
print(f"El promedio es: {res}")