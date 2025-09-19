def potencia():
 print("Calcular la potencia de dous números")
n1 = float(input("Ingrese un número enteiro: "))
n2 = float(input("Ingrese otro número enteiro: "))

if n2. is_integer():
    resultado = 1
    for i in range(int(n2)):
        resultado *= n1
    print(f"La potencia de {n1} elevado a {n2} es: {resultado} ")
else:
    resultado = n1 ** n2
    print(f"La potencia de {n1} elevado a {n2} es: {resultado} ")

print("Es todo por ahora")


potencia()
