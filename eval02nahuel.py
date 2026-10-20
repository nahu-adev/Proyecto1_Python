contraseña = "EST2026"
intentos = 0

while intentos <3:
    codigo = str(input("Ingrese el código de socio: "))
    if codigo == "":
        print("No ingreso código, intente nuevamente.")
        continue
    
    intentos = intentos + 1
    if codigo == contraseña:
        print("Acceso permitido")
        break
    else:
        print(f"Código incorrecto, intento {intentos} de 3")
else:
    print("Acceso denegado, consulte en preceptoría")