# 15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valorPorHora = float(input('Quanto você ganha por hora? '))
horasTrabalhadas = int(input('Horas trabalhadas durante um mês: '))
salarioBruto = valorPorHora * horasTrabalhadas
imposto = (11 / 100 * salarioBruto)
inss = (8 / 100 * salarioBruto)
sindicato = (5 / 100 * salarioBruto)

print('Salário bruto R$ {:.2f}'.format(salarioBruto))
print('Contribuição ao imposto de renda R$ {:.2f}'.format(imposto))
print('Valor descontado ao INSS R$ {:.2f}'.format(inss))
print('Valor descontado ao sindicato R$ {:.2f}'.format(sindicato))
print('Este será o meu salário liquido R$ {:.2f}'.format(salarioBruto - imposto - inss - sindicato))