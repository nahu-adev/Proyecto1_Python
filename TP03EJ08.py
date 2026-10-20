num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otr número: "))

if num1<num2:
    inicio = num1
    final = num2
else:
    inicio = num2
    final = num1
    
for i in range(inicio,final):
    print(i)
    