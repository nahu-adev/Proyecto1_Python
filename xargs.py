def suma(*numeros): #el asterico indica que el parámetro es iterable(for)
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,5,7)
suma(3,6,9)