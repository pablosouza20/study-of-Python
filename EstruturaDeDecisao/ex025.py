'''
25- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A - "Telefonou para a vítima?"
B - "Esteve no local do crime?"
C - "Mora perto da vítima?"
D - "Devia para a vítima?"
E - "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
acumulador = 0

res1 = str(input('Você telefonou para a vítima?\nSim ou Não: ')).lower().strip()
if res1 == 'sim':
  acumulador += 1 
else:
  acumulador += 0  

res2 = str(input('Esteve no local do crime?\nSim ou Não: ')).lower().strip()
if res2 == 'sim':
  acumulador += 1
else:
  acumulador += 0

res3 = str(input('Mora perto da vítima?\nSim ou Não: ')).lower().strip()
if res3 == 'sim':
  acumulador += 1
else:
  acumulador += 0    

res4 = str(input('Devia para a vítima?\nSim ou Não: ')).lower().strip()   
if res4 == 'sim':
  acumulador += 1
else:
  acumulador += 0  

res5 = str(input('Já trabalhou com a vítima?\nSim ou Não: ')).lower().strip()
if res5 == 'sim':
  acumulador += 1
else:
  acumulador += 0  

print('Classificação das suas respostas: {}'.format(acumulador))

if acumulador == 2:
  print('Suspeita')
elif acumulador > 2 and acumulador <= 4:
  print('Cúmplice')
elif acumulador > 4:
  print('Suspeita') 
else:
  print('Inocente')     


'''
Explicação: Eu criei uma variável chamada pontos, e fui adicionando +1 a cada resposta equivalente a "SIM".

Depois usando IF eu fiz relação do total de pontos obtidos com as classificações.

Para finalizar mostrei o total de pontos e a classificação da pessoa.
'''






