# 11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))

dobro = numero1 * 2
metade = numero2 / 2
print(dobro)
print('O produto do dobro do primeiro com metade do segundo: {}'.format(dobro + metade))

triploPrimeiro = numero1 * 3
print('A soma do triplo do primeiro com o terceiro: {:.2f}'.format(triploPrimeiro + numero3))

elevadoAoCubo = numero3**3
print('O terceiro elevado ao cubo: {:.2f}'.format(elevadoAoCubo))