#keyword arguments
def get_product(**datos):
    print(datos["name"])

get_product(id="id", name="Celu", desc="significa celular")