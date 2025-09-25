def farenheit( temperatura ):
    celsius = (temperatura - 32) * 5/9
    return celsius

try:

    tempFahrenheit = float(input("Temperatura Fahrenheit: "))
    tempCelsius = farenheit(tempFahrenheit)
    print( f"{tempFahrenheit}º equivale a {tempCelsius: .2f}ºC")
except ValueError:
    print("el valor no es valido")


----------------------------------------------------------------------------------------------------------------
temperature = input("Temperatura Celsius: ")
temperatura= float(input("Temperatura Celsius: "))
f= 9/5* temperatura + 32
print (f)




