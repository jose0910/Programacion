print("Táboa de conversión de Fahrenheit a Celsius")
print("Fahrenheit   Celsius")

for f in range(0, 121, 10):   # dende 0 ata 120, de 10 en 10
    c = (f - 32) * 5/9
    print(f"{f:10}   {c:7.2f}")
