from funciones import promedio, aprobados
cant=int(input("Cantidad de notas a ingresar: "))
notas=[]

for i in range(cant):
    num=int(input(f"Ingrese nota {i+1}: "))
    notas.append(num)

res=promedio(notas)
print(f"El promedio es {res}")
aprobados(res)