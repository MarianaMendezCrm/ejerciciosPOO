edad = int(input("EDAD: "))


if edad < 12:
    costo = 50
elif 12 <= edad <= 17:
    costo = 80
elif edad >= 18:
    costo = 120




    print(f"EL COSTO DE LA ENTRADA ES: ${costo}")
