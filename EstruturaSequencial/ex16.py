'''16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

import math

tamanho = int(input('Tamanhos em metros quadrado:  '))
litros_usados = tamanho / 3
litros_por_lata = 18
numero_de_latas = math.ceil(litros_usados / litros_por_lata)
valor_com_apenas_latas = numero_de_latas * 80

print('Você deverá usar {} latas de 18 litros, no valor de R$ {:.2f}.'.format(numero_de_latas, valor_com_apenas_latas))