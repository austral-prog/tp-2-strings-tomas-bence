def casting():
    precio = int(input())
    descuento = float(input())
    cantidad = int(input())

    precio_con_descuento = precio - descuento
    total = precio_con_descuento * cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_con_descuento}")
    print(f"Total: {total}")
