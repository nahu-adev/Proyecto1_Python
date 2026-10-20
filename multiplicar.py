num = int(input("Número a multiplicar: "))
limite = int(input("Hasta qué número?: "))
if limite < 1:
    print("El límite debe ser mayor a cero")
else:
    print(f"Tabla del número {num}")
    
    for i in range(1,limite + 1,1):
        resultado = num * i
        if i == limite:
            print(f"{num} x {i} = {resultado} <- ultimo")
        else:
            print(f"{num} x {i} = {resultado}")