def hola(nombre, apellido): #la utilizamos en el contexto de una función. Se denomina Parámetro
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}") #hacemos uso de su parámetro
    
#Aca definimos los argumentos
hola("Nahuel", "Aramayo")
hola("Franco", "Lopez")
hola(apellido="Aramayo", nombre="Lautaro") #podemos nombrar argumentos para establecer el orden del mismo


def saludo():
    print("Bienvenidos")

saludo()

nombre = "Juan"
print("Hola", nombre)

nombre = "Ana"
print("Hola", nombre)

nombre = "Pedro"
print("Hola", nombre)

def saludar(nombre):
    print("Hola", nombre)

saludar("Juan")
saludar("Ana")
saludar("Pedro")

def sumar(a, b):
    return a + b

total = sumar(10, 5) * 2

print(total)


