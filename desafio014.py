#informe a conversao de temperatura de Celcius para Fahrenheit in python

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temperature = float(input("Digite a temperatura em Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"A temperatura em Fahrenheit é: {fahrenheit_temperature:.2f}")

c=float(input('Inform a teperatura em C:'))
f = 9 * c / 5 + 32
print('A temperatura de {}C corresponde a {}F'.format(c, f))