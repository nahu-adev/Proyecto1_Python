a=int(input("Ingrese un nro: "))
b=int(input("Ingrese un nro: "))
c=int(input("Ingrese un nro: "))

if a>b and a>c:
    print(f"El mayor es {a}")
    if b>c:
        print(f"el del medio es {b} y el menor es {c}")
    else:
        print(f"el del medio es {c} y el menor es {b}")
elif b>a and b>c:
    print(f"el mayor es {b}")
    if a>c:
        print(f"el del medio es {a} y el menor es {c}")
    else:
        print(f"el del medio es {c} y el menor es {a}")
elif c>a and c>b:
    print(f"El mayor es {c}")
    if a>b:
        print(f"El del medio es {a} y el menor es {b}")
    else:
        print(f"El del medio es {b} y el menor es {a}")