def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio=int(input("Ingrese el precio: "))
    descuento=float(input("Ingrese el descuento: "))
    cantidad=int(input("Ingrese el cantidad: "))
    preciocondescuento=precio-descuento
    total=preciocondescuento * cantidad
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {preciocondescuento}")
    print(f"Total: {total}")
casting()