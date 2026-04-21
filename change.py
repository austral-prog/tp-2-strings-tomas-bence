def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)

    print("Dinero recibido")
    dinero = float(input())
    print(int(dinero))

    vuelto = dinero - gasto
    pesos = int(vuelto)
    centavos = int(((vuelto - pesos) * 100) + 0.5)

    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
change()