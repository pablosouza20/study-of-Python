'''
7- Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3:
  print('O primeiro número é o maior {}.'.format(num1))
elif num2 > num1 and num2 > num3:
  print('O segundo número é o maior {}.'.format(num2))
elif num3:
  print('O terceiro número é o maior {}.'.format(num3))    