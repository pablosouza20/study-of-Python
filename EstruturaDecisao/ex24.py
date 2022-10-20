-'''
24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a- par ou ímpar;
b- positivo ou negativo;
c- inteiro ou decimal.
'''
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
escolha = str(input('Você terá 3 opções para poder escolher!\nA - par ou ímpar | B - positivo ou negativo | C - inteiro ou decimal: ')).strip().upper()

if escolha == 'A':
    if num1 % 2 == 0:
        print('O número {} é PAR.'.format(num1))
    else:
        print('O número {} é ÍMPAR.'.format(num1))            
    if num2 % 2 == 0:
        print('O número {} é PAR.'.format(num2))
    else:
        print('O número {} é ÍMPAR.'.format(num2))        

if escolha == 'B':
    if num1 > 0:
        print('O número {} é POSITIVO.'.format(num1))
    else:
        print('O número {} é NEGATIVO.'.format(num1))
    if num2 > 0:
        print('O número {} é POSITIVO.'.format(num2))
    else:
        print('O número {} é NEGATIVO.'.format(num2))                   

if escolha == 'C':
    if num1 % 1 == 0:
        print('O número {} é INTEIRO.'.format(num1))
    else:
        print('O número {} é DECIMAL.'.format(num1)) 
    if num2 % 1 == 0:
        print('O número {} é INTEIRO.'.format(num2))
    else:
        print('O número {} é DECIMAL.'.format(num2))    