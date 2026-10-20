for i in range(1, 11):
    if i == 7:
        break
    print(i)

numeros = [3, 8, 2, 10, 5]
for n in numeros:
    if n == 10:
        print("Encontrado")
        break

while True:
    texto = str(input("Escribe algo: "))
    if texto == "salir":
        break
    print(texto)
    
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)