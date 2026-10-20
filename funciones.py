def saludar(nombre):
    print(f"Hola {nombre}")

def sumar(a, b):
    return a + b

def producto(a,b):
    return a*b

def cociente(a,b):
    return a/b

def promedio(lista):
    suma=sum(lista)
    promedio=suma/len(lista)
    return promedio

def superficie(base,altura):
    sup=base*altura/2
    return sup

def porcentaje(valor,total):
    porc = valor*100/total
    return porc

def mayormenor(a,b):
    if a>b:
        print(f"El mayor es {a} y el menor es {b}")
    else:
        print(f"El mayor es {b} y el menor es {a}")

def sexo(cond):
    if cond.lower() == "m":
        print("Masculino")
    else:
        print("Femenino")
        
def aprobado(nota):
    if nota>=6:
        print("Aprobado")
    else:
        print("Desaprobado")        
        
def cero(a):
    if a>0:
        print(f"El número {a} es mayor a cero")
    elif a<0:
        print(f"El número {a} es menor a cero")
    else:
        print(f"El número {a} es igual a cero")
        
def aprobados(a):
    if a>=7:
        print("Aprobado")
    elif a<4:
        print("A marzo")
    else:
        print("A diciembre")