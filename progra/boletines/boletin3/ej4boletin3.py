#pide 2 nombres y sus respectivos pesos
persona1 = input("Ingresa un nombre: ")
persona2 = input("Ingresa un nombre: ")
pesop1 = int(input(f"Ingresa el peso de {persona1}: "))
pesop2 = int(input(f"Ingresa el de {persona2}: "))

#muestra el nombre, peso y la diferencia de pesos de la persona que pesa mas
if pesop1 > pesop2:
    print (persona1 , pesop1)
    print(persona1, "pesa", pesop1 - pesop2,"kg", "mas que", persona2)
else:
    print(persona2, pesop2)
    print(persona2, "pesa", pesop2 - pesop1,"kg", "mas que", persona1)