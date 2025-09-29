import math

def CrearMenu():
    print("Menú de opcións:")
    print("1 - Cadrado")
    print("2 - Triángulo")
    print("3 - Círculo")
    print("4 - Saír")

def calcularAreaCuadrado(base, altura):
    return base * altura

def calcularAreaTriangulo(base, altura):
    return calcularAreaCuadrado(base, altura) / 2

def calcularAreaCirculo(radio):
    return math.pow(radio, 2) * math.pi

def recollerParanetros(opcion):
    if opcion == 1 or opcion == 2:
        base = float(input("Introduce la base: "))
        altura = float(input("Introduce la altura: "))
        return base, altura
    elif opcion == 3:
        radio = float(input("Introduce el radio: "))
        return radio

def exercicioBoletin4_2():
    opcion = 0
    while opcion != 4:
        CrearMenu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1 or opcion == 2:
            base, altura = recollerParanetros(opcion)
            if opcion == 1:
                area = calcularAreaCuadrado(base, altura)
                print("El área del cuadrado es:", area)
            else:
                area = calcularAreaTriangulo(base, altura)
                print("El área del triángulo es:", area)
        elif opcion == 3:
            radio = recollerParanetros(opcion)
            area = calcularAreaCirculo(radio)
            print("El área del círculo es:", area)
        elif opcion == 4:
            print("Saíndo do programa...")
        else:
            print("Opción inválida")

exercicioBoletin4_2()
