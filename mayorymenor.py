
num1 = float(input("PRIMER NUMERO: "))
num2 = float(input("SEGUNDO NUMERO: "))
num3 = float(input("TERCER NUMERO: "))


if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3


if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3


print(f"\nEL MAYOR ES: {mayor}")
print(f"EL MENOR ES: {menor}")