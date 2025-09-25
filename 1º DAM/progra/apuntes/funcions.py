#grupo de funciones que tienen una utilidad, las vamos a llamar por un nombre
#calculos pequeños con un fin concreto
#se declara una funcion poniendo-----> def funcion():
#


def crearMenu():
    print("Menú de opcións:")
    print("1 - Cadrado")
    print("2 - Triángulo")
    print("3 - Círculo")

crearMenu()

def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2
    return area

crearMenu()
AreaTriangulo = calcularAreaTriangulo(base=4, altura=3)
print("Área do triángulo:", AreaTriangulo)



