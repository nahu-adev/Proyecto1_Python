nom = str(input("Ingrese su nombre completo: "))
edad = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese el promedio obtenido en la escuela anterior: "))
print(f"Bienvenido {nom}")
if promedio >=7:
    print("Ingreso directo")
elif promedio >=4:
    print("Debe rendir un examen de nivelación")
else:
    print("Debe ir a curso de apoyo")