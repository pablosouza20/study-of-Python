'''
26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a - Álcool:
b - até 20 litros, desconto de 3% por litro
c - acima de 20 litros, desconto de 5% por litro
d - Gasolina:
e - até 20 litros, desconto de 4% por litro
f - acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''
print('Posto de combustível')
opcao = str(input('Escolha entre A-álcool ou G-gasolina para selecionar o seu combustível: ')).strip().upper()
litros = float(input('Quantos litros deverá ser colocado? '))

if opcao == 'A':
    preco = litros * 4.89
    if litros <= 20: 
            desconto = preco - (preco * 3/100)
    else:
            desconto = preco - (preco * 5/100)
if opcao == 'G':
    preco = litros * 6.58
    if litros <= 20:
            desconto = preco - (preco * 4/100)
    else:
            desconto = preco - (preco * 6/100)     

print('Preço normal sem desconto R$ {:.2f}'.format(preco))
print('Preço com desconto aplicado R$ {:.2f}'.format(desconto))

