a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))

if a>b:
    alto = a
    bajo = b
else:
    alto = b
    bajo = a

for i in range(bajo,alto,1):
    print(i)