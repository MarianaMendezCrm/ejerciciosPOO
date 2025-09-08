
calificacion = int(input("INGRESE SU CALIFICACION: "))

#
if 90 <= calificacion <= 100:
    print("LA CALIFICACION EQUIVALE: A")
elif 80 <= calificacion <= 89:
    print("LA CALIFICACION EQUIVALE: B")
elif 70 <= calificacion <= 79:
    print("LA CALIFICACION EQUIVALE: C")
elif 60 <= calificacion <= 69:
    print("LA CALIFICACION EQUIVALE: D")
elif 0 <= calificacion < 60:
    print("LA CALIFICACION EQUIVALE: F")
