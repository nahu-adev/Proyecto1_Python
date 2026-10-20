#Ejemplo básico de ciclo
#for numero in range(6):
#    print(numero)
    
#Replicar el mismo nombre 5 veces
#nombre = str(input("Ingrese un nombre: "))
#for i in range(5):
#    print(nombre)

#identación = sangría
#iteración = cantidad de veces que se ejecuta el ciclo
    
#Para x desde 1 hasta 10 con paso 1 hacer
    #Acción del ciclo
#FinPara

#Escribir nombres de una lista
#in = dentro de
#menu = ["hamburguesa","milanesa","pizza","lomito"]
#for x in menu:
#    print(f"La comida de hoy es {x}")
    
#x en la iteracion 0 = hamburguesa
#x en la iteracion 1 = milanesa
#x en la iteracion 2 = pizza
#x en la iteracion 3 = lomito

#contador = 0
#while contador <5:
#    print(contador)
#    contador +=1

#contador = 0
#contador = contador + 1

#contador = 0 + 1
#contador = 1

#contador = 1 + 1
#contador = 2

#PRESTAR ATENCIÓN A LA HORA DE UTILIZAR CICLOS INFINITOS
#while True:
#    print("Hola mundo")

#Establecer el rango de inicio, el final y el paso
#for i in range(0,21,3):
#    print(i)

#BREAK : Salir del ciclo aunque este no haya terminado
#for x in range(11):
#    if x == 5:
#        break
#    print(x)

#print("Ciclo terminado")

#CONTINUE : Salta la iteración y sigue con el siguiente
#for i in range(6):
#    if i == 2:
#        continue
#    print(i)

#Ejemplo de contador con while y break
#contador = 0
#while True:
#    if contador == 3:
#        break
#    print(contador)
#    contador += 1
    
#print(f"Contador finalizado en el número {contador}")

#Ejemplo de while y continue
#num = 0
#while num <10:
#    num +=1
#    if num == 5:
#        continue
#    print(num)

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otr número: "))

if num1<num2:
    for i in range(num1,num2):
        print(i)
else:
    for i in range(num2,num1):
        print(i)