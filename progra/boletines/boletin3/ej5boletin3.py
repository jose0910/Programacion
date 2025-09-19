num1 = int(input("digite numero:"))
num2 = int(input("digite numero:"))
num3 = int(input("digite numero:"))

if num1 > num2 and num1 > num3:
    print(num1, "es el numero mas grande")
elif num2 > num3:
    print(num2, "es el numero mas grande")
else:
    print(num3, "es el numero mas grande")

