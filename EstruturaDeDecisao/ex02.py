'''
2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
num = float(input('Digite qualquer valor sendo ele positivo ou negativo: '))
if num >= 0:
    print('O número {:.2f} é postivo!'.format(num))
else:
    print('O número {:.2f} é negativo!'.format(num))    
