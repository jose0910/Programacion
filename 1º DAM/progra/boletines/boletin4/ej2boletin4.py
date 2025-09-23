import math

print("Menú de opcións:")
print("1 - Cadrado")
print("2 - Triángulo")
print("3 - Círculo")

opcion = input("Escolle unha opción (1-3): ")

if opcion == "1":
    lado = float(input("Introduce o lado do cadrado: "))
    area = lado * lado
    print(f"A superficie do cadrado é {area}")

elif opcion == "2":
    base = float(input("Introduce a base do triángulo: "))
    altura = float(input("Introduce a altura do triángulo: "))
    area = (base * altura) / 2
    print(f"A superficie do triángulo é {area}")

elif opcion == "3":
    radio = float(input("Introduce o radio do círculo: "))
    area = math.pi * radio**2
    print(f"A superficie do círculo é {area:.2f}")

else:
    print("Opción incorrecta")
