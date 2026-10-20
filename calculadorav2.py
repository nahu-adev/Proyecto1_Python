cantidad = int(input("¿Cuántas notas vas a ingresar?:"))
total = 0
contador = 0
for i in range(cantidad):
    nota = int(input(f"Ingrese la nota {i+1}: "))
    if nota < 0 or nota > 10:
        print("Nota inválida, se omite.")
        continue
    total += nota
    contador +=1
    if contador ==0:
        print("No se ingresaron notas válidas")
    else:
        promedio = total / contador
        print(f"Promedio: {promedio:.2f}")
        
    if promedio >=9:
        print("Excelente")
    elif promedio >=6:
        print("Aprobado")
    else:
        print("Desaprobado")