# 8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Quanto você ganha por hora? '))
horasTrab = int(input('Número de horas trabalhadas durante o mês? '))
salario = valorHora * horasTrab

print('Salário após um mês cheio de serviço R$ {:.2f}'.format(salario))