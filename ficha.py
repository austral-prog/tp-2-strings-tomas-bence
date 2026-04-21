def ficha():
    encabezado = """========================
    FICHA DEL ALUMNO
========================"""

    nombre = input("Ingrese su nombre completo: ")
    nombre_limpio = nombre.strip().title()
    pos_espacio = nombre_limpio.find(" ")
    nombre_pila = nombre_limpio[:pos_espacio]
    apellido = nombre_limpio[pos_espacio + 1:]

    email = input("Ingrese su email: ")
    email_limpio = email.strip().lower()
    dominio = email_limpio[email_limpio.find("@") + 1:]

    nota1 = int(input("Ingrese su nota 1: "))
    nota2 = int(input("Ingrese su nota 2: "))
    nota3 = int(input("Ingrese su nota 3: "))

    print(encabezado)
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_limpio}")
    print(f"Caracteres en nombre: {len(nombre_limpio)}")
    print(f"Iniciales: {nombre_limpio[0]}{nombre_limpio[pos_espacio + 1]}")
    print(f"Usuario: {apellido.lower()}.{nombre_pila.lower()}")
    print(f"Email valido: {'@' in email_limpio}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_limpio.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre_limpio.lower().count('a')}")
    print(f"Codigo secreto: {nombre_limpio[::-1].upper()}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma: {nota1 + nota2 + nota3}")
    print(f"Promedio: {(nota1 + nota2 + nota3) / 3}")
    print(f"Promedio entero: {(nota1 + nota2 + nota3) // 3}")
    print("=" * 24)
