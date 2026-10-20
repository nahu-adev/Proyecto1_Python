nombre = str(input("Ingrese un nombre:"))
print(f"Bienvenido {nombre}")

n1=int(input("Ingrese un nro:"))
n2=int(input("Ingrese otro nro:"))
sum=n1+n2
print(f"El resultado es {sum}")

n3=int(input("Ingrese un nro:"))
n4=int(input("Ingrese otro nro:"))
mul=n3*n4
div=n3/n4
print(f"La multiplicación es {mul}")
print(f"La división es {div}")

base=int(input("Ingrese la base de un triangulo:"))
altura=int(input("Ingrese la altura de un triangulo:"))
sup=base*(altura/2)
print(f"La superficie es {sup}")

var=int(input("Ingrese cantidad de varones:"))
muj=int(input("Ingrese cantidad de mujeres:"))
total=var+muj
pvar=var*100/total
pmuj=muj*100/total
print(f"El porcentaje de varones es {pvar} y el porcentaje de mujeres es {pmuj}")

a=int(input("Ingrese un nro:"))
b=int(input("Ingrese un nro:"))
if a>b:
    print(f"El mayor es {a} y el menor es {b}")
else:
    print(f"El mayor es {b} y el menor es {a}")
