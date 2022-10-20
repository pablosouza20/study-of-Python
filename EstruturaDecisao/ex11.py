-'''
11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
'''

salario = float(input('Digite o salário do funcionário R$ '))

if salario <= 280.00:
  novoSalario = salario + (salario * 20/100)
  aumento = novoSalario - salario
  print('Foi aplicado um percentual de 20% no salário.')

elif salario > 280.00 and salario <= 700.00:
  novoSalario = salario + (salario * 15/100)
  aumento = novoSalario - salario
  print('Foi aplicado um percentual de 15% no salário.')
  
elif salario > 700.00 and salario <= 1.500:
  novoSalario = salario + (salario * 10/100)
  aumento = novoSalario - salario
  print('Foi aplicado um percentual de 10% no salário.')

elif salario > 1.500:
  novoSalario = salario + (salario * 5/100) 
  aumento = novoSalario - salario
  print('Foi aplicado um percentual de 10% no salário.')   

print('Salário antes do reajuste: R$ {:.2f}'.format(salario))
print('Valor do aumento do salário R$ {:.2f}'.format(aumento))
print('Novo salário após aumento R$ {:.2f}'.format(novoSalario))  