from funciones import porcentaje

var=int(input("Ingrese cantidad de varones: "))
muj=int(input("Ingrese cantidad de mujeres: "))
total = var+muj
resv=porcentaje(var,total)
resm=porcentaje(muj,total)
print(f"El porcentaje de varones es de {resv} y el porcentaje de mujeres es de {resm}")