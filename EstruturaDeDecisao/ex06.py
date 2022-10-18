'''
06 - Faça um programa que leia três números e mostre o maior deles
'''
num1 = float(input('Digite um número qualquer: '))
num2 = float(input('Digite um número qualquer: '))
num3 = float(input('Digite um número qualquer: '))

if num1 > num2 and num1 > num3:
    print('O maior número é {}.'.format(num1))
elif num2 > num1 and num2 > num3:
    print('O maior número é {}.'.format(num2))
else:
    print('O maior número é {}.'.format(num3))        