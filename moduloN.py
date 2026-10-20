import math #Este módulo proporciona acceso a funciones y constantes matemáticas comunes, incluidas las definidas por el estándar C.

print(round(1.3))          # Redondea 1.3 al entero más cercano → 1
print(round(1.7))          # Redondea 1.7 al entero más cercano → 2
print(round(1.49))          # Redondea 1.5 al entero más cercano → 2
print(abs(-23))            # Retorna el valor absoluto de -23 → 23
print(abs(45))             # Retorna el valor absoluto de 45 → 45

print(math.ceil(1.2))      # Redondea hacia ARRIBA al entero más cercano → 2
print(math.floor(1.9999))  # Redondea hacia ABAJO al entero más cercano → 1
print(math.isnan(23))      # Verifica si el valor es NaN (Not a Number) → False
#print(math.isnan("23"))   # Daría error porque "23" es un string, no un número
print(math.pow(10,2))      # Calcula 10 elevado a la potencia 2 → 100.0
print(math.sqrt(9))        # Calcula la raíz cuadrada de 9 → 3.0
print(math.cbrt(8))