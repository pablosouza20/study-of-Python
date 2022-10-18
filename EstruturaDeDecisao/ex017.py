'''
17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
'''
ano = int(input('Digite um ano para verificarmos se é bissexto ou não: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano {} é bissexto.'.format(ano))
else:
    print('Ano {} não é bissexto'.format(ano))    

     