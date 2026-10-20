palabra = " hola mundo "

print(palabra.upper())           # Convierte todos los caracteres a MAYÚSCULAS
print(palabra.lower())           # Convierte todos los caracteres a minúsculas
print(palabra.strip())           # Elimina espacios en blanco al inicio y al final
print(palabra.capitalize())      # Pone en mayúscula solo el primer carácter de la cadena
print(palabra.title())           # Pone en mayúscula la primera letra de cada palabra
print(palabra.upper())           # Convierte todos los caracteres a MAYÚSCULAS
print(palabra.lstrip())          # Elimina espacios en blanco solo al inicio (izquierda)
print(palabra.rstrip())          # Elimina espacios en blanco solo al final (derecha)
print(palabra.find("la"))        # Busca "la" y retorna el índice donde comienza, o -1 si no existe
print(palabra.replace("do","dial")) # Reemplaza la subcadena "do" por "dial" en la cadena
print("mun" in palabra)          # Verifica si "mun" está contenido en la cadena, retorna True o False
print("mun" not in palabra)      # Verifica si "mun" NO está contenido en la cadena, retorna True o False