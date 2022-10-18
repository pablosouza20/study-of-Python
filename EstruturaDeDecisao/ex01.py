'''
1- Faça um Programa que peça dois números e imprima o maior deles.
'''
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if num1 > num2:
  print('Este é o maior número: {:.2f}'.format(num1))
else:
  print('Este é o maior número: {:.2f}'.format(num2))  
  