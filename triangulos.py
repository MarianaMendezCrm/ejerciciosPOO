lado1 = float(input("PRIMER LADO: "))
lado2 = float(input("SEGUNDO LADO: "))
lado3 = float(input("TERCER LADO: "))


if lado1 == lado2 == lado3:
    print("EL TRIANGULO ES EQUILATERO")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("EL TRIANGULO ES ISOSELES")
else:
    print("EL TRIANGULO ES ESCALENO")