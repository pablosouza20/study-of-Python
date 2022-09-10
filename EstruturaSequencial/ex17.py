''' 17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''

import math

# Compra de tinta somente com latas de 18 litros.
tamanho = int(input('Tamanhos em metros quadrado:  '))
area_com_folga = tamanho * 1.1
litros_usados = area_com_folga / 6
litros_por_lata = 18
numero_de_latas = math.ceil(litros_usados / litros_por_lata)
valor_com_apenas_latas = numero_de_latas * 80
print('Você deverá usar {} latas de 18 litros, no valor de R$ {:.2f}.'.format(numero_de_latas, valor_com_apenas_latas))

# Compra de tinta somente com galões de 3,6 litros
litros_por_galao = 3.6
numero_de_galoes = math.ceil(litros_usados / litros_por_galao)
valor_com_apenas_galoes = numero_de_galoes * 25
print('Você deverá usar {} galões de 3.6 litros, no valor de R$ {:.2f}.'.format(numero_de_galoes, valor_com_apenas_galoes))

# Forma otimizada para compra tinta por valor
numero_de_latas = math.floor(litros_usados / litros_por_lata)
valor_de_latas = numero_de_latas * 80
litros_faltantes = litros_usados % litros_por_lata
numero_de_galoes = math.ceil(litros_faltantes / litros_por_galao)
valor_com_galoes = numero_de_galoes * 25
valor_total = valor_de_latas + valor_com_galoes
print('Você deverá usar {} latas de 18 litros mais {} galões de 3.6 litros, no valor de R$ {:.2f}.'.format(numero_de_latas, numero_de_galoes, valor_total))