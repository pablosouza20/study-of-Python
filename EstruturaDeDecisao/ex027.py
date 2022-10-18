'''
27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
print('Bem-vindo a fruteira do Ben-ti-vi')
pesoMorango = float(input('Informe quantos quilos de morango adquiridos: '))
pesoMaca = float(input('Informe quantos quilos de maçã adquiridos: '))
print('Peso do morango: {:.1f} Kg.\nPeso da maçã: {:.1f} Kg.'.format(pesoMorango, pesoMaca))

precoMorango1 = pesoMorango * 2.50                                      # Até 5 Kg / Preço 2,50 por Kg
precoMorango2 = pesoMorango * 2.20                                      # Acima 5 Kg / Preço 2,20 por Kg

precomaca1 = pesoMaca * 1.80                                            # Até 5 Kg / Preço 1,80 por Kg
precomaca2 = pesoMaca * 1.50                                            # Acima 5 Kg / Preço 1,50 por Kg

# IF que faz o cálculo dos preços até 5 Kg do morango e maça
if pesoMorango > 5:
    precoCertoMorango = precoMorango1   
else:
    precoCertoMorango = precoMorango2    

if pesoMaca > 5:
    precoCertoMaca = precomaca1
else:
    precoCertoMaca = precomaca2    

valorTotal = precoCertoMorango + precoCertoMaca    
print(valorTotal)

if valorTotal > 25 or (pesoMorango + pesoMaca) > 8:
    print('Senhor(a) cliente está levando {:.1f} Kg de morango e {:.1f} Kg de maça.\nO preço total dos dois produtos a ser pago já com desconto aplicado R$ {:.2f}'.format(pesoMorango, pesoMaca, (valorTotal - (valorTotal * 10/100))))
else:
    print('Senhor(a) cliente está levando {:.1f} Kg de morango e {:.1f} Kg de maça.\nO preço total dos dois produtos a ser pago R$ {:.2f}'.format(pesoMorango, pesoMaca, valorTotal))

