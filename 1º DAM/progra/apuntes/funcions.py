#tienen una utilidad, las vamos a llamar por un nombre
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



def suma(n1, n2, *outrosNumeros):
    suma = n1 + n2
    for n in outrosNumeros:
        suma = suma + n
        return suma

print(suma(n1=3, n2=2 ))


def datosPersoa (dni, nome, **datosExtendidos):
    print ("O dni é ", dni)
    print ("O nome é ", nome)
    for k, v in datosExtendidos.items():
        print( k, "é", v )


datosPersoa(dni="333J", nome="Jose", altura= 1.82, peso = 75)




