# 10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

grausCelsius = int(input('Informe quantos graus em celsius: '))

F = (grausCelsius*1.8000) + 32.00

print('Conversão de graus {}ºG para graus {:.0f}ºF.'.format(grausCelsius, F))