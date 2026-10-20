nombre = str(input("Ingrese un nombre de usuario: "))
palabra = nombre.strip()

if len(palabra)<5:
    print("Es un nombre corto")  
elif "admin" in palabra:
    print("Nombre no permitido")
else:
    print(palabra.title(),"Usuario válido")