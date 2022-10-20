-'''
28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                Até 5 Kg                Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a 
quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''
print('Bem-vindo ao mercado Tabajara')
print('File Duplo até 5kg, custa R$ 4,90 e acima de 5Kg, custa R$ 5,80.')
print('Alcatra até 5kg, custa R$ 5,90 e acima de 5Kg, custa R$ 6,80.')
print('Picanha até 5kg, custa R$ 6,90 e acima de 5Kg, custa R$ 7,80.')
tipoCarne = str(input('Informe o tipo da carne que você quer comprar, selecionando "A" para File Duplo | "B" para Alcatra | "C" para Picanha: '))
quantidade = float(input('Informe quantos quilos carne será comprado: '))

precoFileDuplo1 = quantidade * 4.90 
precoFileDuplo2 = quantidade * 5.80

precoAlcatra1 = quantidade * 5.90
precoAlcatra2 = quantidade * 6.80

precoPicanha1 = quantidade * 6.90
precoPicanha2 = quantidade * 7.80

if tipoCarne == 'a':
    tipoCarne = 'Filé Duplo'
    if quantidade > 5:
        precoTotal = precoFileDuplo2
    else:
        precoTotal = precoFileDuplo1
   
if tipoCarne == 'b':
    tipoCarne = 'Alcatra'
    if quantidade > 5:
        precoTotal = precoAlcatra2
    else:
        precoTotal = precoAlcatra1
   
if tipoCarne == 'c':
    tipoCarne = 'Picanha'
    if quantidade > 5:
        precoTotal = precoPicanha2
    else:
        precoTotal = precoPicanha1        
    
print('Nota fiscal')
print('Tipo da carne: {}\nQuantidade de carne: {} Kg\nPreço total do produto R$ {:.2f}'.format(tipoCarne, quantidade, precoTotal))

tipoPagamento = str(input('Se o pagamento for no cartão Tabajara, terá um desconto de 5%.\nDigite "Sim" para continuar ou "Não" para finalizar: '))
if tipoPagamento == 'sim':
    tipoPagamento = 'Cartão tabajara'
    valorFinal = precoTotal - (precoTotal * 5/100)
    desconto = precoTotal - valorFinal 
    print('Tipo do pagamento: {}\nValor do desconto R$ {:.2f}\nValor com desconto aplicado R$ {:.2f}'.format(tipoPagamento, desconto, valorFinal)) 
else:
    print('Compra concluída.')
 