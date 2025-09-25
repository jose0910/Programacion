t= ( 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 )
i= 0
suma = 0
while i <= 7:
    suma = suma + t[i]
    i += 1 # i = i + 1
    print(suma)

print(suma, i)


for numero in t:
    print(numero)
    suma = suma + numero

print(suma)

for i in range(0, 7):
    print(i)
    print(t[i])

for i, numero in enumerate(t):
    print(i)
    print(numero)
    print(t[i])



print("start bucle")
iteracion = 1
for numero in t:
    print("iteracion",iteracion)
    print("elemento da tupla",numero)
    print("incremento i")
    iteracion = iteracion + 1


print("final")