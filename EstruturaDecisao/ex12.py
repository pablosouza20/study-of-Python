-'''
12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900  (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
       - Salário Bruto: (5 * 220)        : R$ 1100,00
       - (-) IR (5%)                     : R$   55,00  
       - (-) INSS ( 10%)                 : R$  110,00
       - FGTS (11%)                      : R$  121,00
       - Total de descontos              : R$  165,00
       - Salário Liquido                 : R$  935,00
'''
valorHora = int(input('Digite o valor da sua hora: '))
horasTrabalhadas = int(input('Digite a quantidade de horas trabalhadas no mês: '))
salarioBruto = horasTrabalhadas * valorHora

if salarioBruto <= 900:
  print('Você está isento dos descontos!')
  print('Seu salário é de R$ {:.2f}'.format(salarioBruto))
elif salarioBruto > 900 and salarioBruto <= 1500:
  ir =   (salarioBruto * 5/100) 
   
elif salarioBruto > 1500 and salarioBruto <= 2500:
  ir =   (salarioBruto * 10/100) 
  
elif salarioBruto > 2500:
  ir =   (salarioBruto * 20/100) 
 
inss = (salarioBruto * 10/100)
fgts = (salarioBruto * 11/100) 
totalDescontos = ir + inss
salaLiquido = salarioBruto - totalDescontos

print('Salário bruto R$ {:.2f}'.format(salarioBruto))
print('Desconto do imposto de renda R$ {:.2f}'.format(ir))
print('Desconto do INSS R$ {:.2f}'.format(inss))
print('O FGTS é a empresa que deposita R$ {:.2f}'.format(fgts))
print('Total de descontos R$ {:.2f}'.format(totalDescontos))
print('Salário liquido R$ {:.2f}'.format(salaLiquido))   