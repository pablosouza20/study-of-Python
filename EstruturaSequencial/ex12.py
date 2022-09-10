# 12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite a sua altura: '))

print('Com dados referente a sua altura que é {} cm , esse seria o seu peso ideal: {:.2f} Kg'.format(altura, (72.7*altura)-58))