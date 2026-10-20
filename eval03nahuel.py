materiales = []
cantidad = int(input("¿Cuántos materiales desea ingresar?: "))

for i in range(cantidad):
    material = input(f"Ingrese material nro{i+1}: ")
    if material in materiales: 
        print("El material ya fue agregado")
        continue
    materiales.append(material)

for i in range(len(materiales)):
    print(f"Material {i+1}: {materiales[i]}")

print(f"Total de materiales cargados: {len(materiales)}")

materiales.sort()
print("Mostrar materiales ordenados alfabéticamente:")
print(materiales)
    
materiales.reverse()
print("Mostrar materiales en reversa:")
print(materiales)