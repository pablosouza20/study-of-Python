-'''
23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''
num = float(input('Digite um número qualquer: '))
if num % 1 == 0:
    print('Inteiro')
else:
    print('Decimal')    
