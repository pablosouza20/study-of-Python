'''
21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''
print('O valor mínimo para sacar é de R$ 10 e o máximo é de R$ 600')
valorSaque = int(input('Digite o valor que você quer sacar R$ '))

if valorSaque >= 10 and valorSaque <= 600:
    nota100 = valorSaque // 100
    resto100 = valorSaque % 100
    nota50 = resto100 // 50
    resto50 = resto100 % 50
    nota10 = resto50 // 10
    resto10 = resto50 % 10
    nota1 = resto10 // 1
if nota100 != 0:
    print('O programa fornece {} notas de 100,'.format(nota100), end= ' ') 
if nota50 != 0:
    print('{} notas de 50,'.format(nota50), end= ' ')
if nota10 != 0:
    print('{} notas de 10,'.format(nota10), end= ' ')  
if nota1 != 0:
    print('{} notas de 1.'.format(nota1))        

print('Para sacar a quantia de R$ {}.'.format(valorSaque))    