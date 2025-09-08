
año = int(input("INGRESA UN AÑO: "))


if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"EL AÑO {año} ES BISIESTO")
else:
    print(f"EL AÑO {año} NO ES BISIESTO")