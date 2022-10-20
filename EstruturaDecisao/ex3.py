-'''
3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = str(input('Digite "F" para feminino ou "M" para masculino: ')).strip().upper()

if sexo == 'F':
  print('Pessoa do sexo feminino!')
elif sexo == 'M':
  print('Pessoa do sexo masculino!')
else:
  print('Sexo inválido!')