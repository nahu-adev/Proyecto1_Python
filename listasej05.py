notas = []

cant = int(input("¿Cuántas notas desea ingresar?: "))
for i in range (cant):
    val = int(input(f"Ingrese la nota n°{i+1}: "))
    notas.append(val)
    
total = 0
for x in notas:
    total = total + x

promedio = total / cant

if promedio >=6:
    print(f"Alumno aprobado con nota: {promedio}")
else:
    print(f"Alumno desaprobado con nota: {promedio}")