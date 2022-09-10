# 13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite a sua altura: '))

print('Essa é sua altura {} cm. Se você for homem, esse será o seu peso ideal: {:.2f} Kg'.format(altura, (72.7*altura)-58))
print('Essa é sua altura {} cm. Se você for mulher, esse será o seu peso ideal: {:.2f} Kg'.format(altura, (62.1*altura)-44.7))