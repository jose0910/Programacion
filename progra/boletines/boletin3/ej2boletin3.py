from textwrap import shorten

num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa un numero: "))

while num1 > num2:
    num1 = float(input("Ingresa un numero: "))

if num1 > num2:
    print (num1 -= num2)
else:
    print (num1 + num2)




    ----------------------------
    num1 = float(input("digite numero:"))
    num2 = float(input("digite numero:"))
    num3 = float(input("digite numero:"))

    if num1 > num2 and num1 > num3:
        print(num1 + "es el numero mas grande")
    elif num2 > num3:
        print(num2 + "es el numero mas grande")
    else:
        print(num3 + "es el numero mas grande")