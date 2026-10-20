print("CALCULADORA")
print("Para cerrar la calculadora escribe salir")
print("Ingrese operación: suma, resta, multiplicacion y division")

resultado="" 
while True:
    if not resultado: #si no hay valores en resultado
        resultado=input("Ingrese número: ") #Pedimos que ingrese un dato pero todavia no determinamos si es entero
        if resultado.lower() == "salir": #si resultado almacena el dato salir entonces hacemos el break
            break
        resultado = int(resultado)  #Si esta fuera del break, debemos transformar el dato ingresado a entero
    
    operacion = input("Ingrese operación: ")
    if operacion.lower() == "salir": #si la operacion es salir, el programa se cierra
        break
    
    n2=input("Ingresa siguiente número: ")
    if n2.lower() == "salir": #si el numero 2 es salir, el programa se cierra
        break
    n2 = int(n2)    #otorgamos al numero como valor entero
    
    if operacion.lower() == "suma":
        resultado += n2
    elif operacion.lower() == "resta":
        resultado -= n2
    elif operacion.lower() == "multiplicacion":
        resultado *= n2
    elif operacion.lower() == "division":
        resultado /= n2
    else:
        print("Operación no válida")
        break
    
    print(f"El resultado es {resultado}")