# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

F = float(input('Informe os graus em Fahrenheit: '))

Celsius = 5 * ((F-32)/9)

print('Conversão de graus {}ºF para graus {:.0f}ºC.'.format(F, Celsius))

