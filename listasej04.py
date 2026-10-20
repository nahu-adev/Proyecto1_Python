puntajes = []

cant = int(input("¿Cuántos puntajes desea ingresar?: "))
for i in range (cant):
    num = int(input(f"Ingrese el puntaje n°{i+1}: "))
    puntajes.append(num)

puntajes.sort()
puntajes.reverse()
print(f"Podio: 1° lugar: {puntajes[0]}, 2° lugar: {puntajes[1]} y 3° lugar: {puntajes[2]}")