'''
4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = str(input('Digite alguma letra para verificarmos se é vogal ou consoante: ')).strip().upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
  print('A letra {} é VOGAL!'.format(letra))
else:
  print('A letra {} é CONSOANTE!'.format(letra))