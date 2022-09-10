# 14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoLimite = 50
pesoPeixe = int (input('Peso dos peixes que o seu João trouxe: '))
if pesoPeixe > pesoLimite:
  excessoPeixe = pesoPeixe - pesoLimite
  multa = excessoPeixe * 4
  
  print('A quantidade permitida para trazer peixes é de 50 quilos determinados pelo Estado de São Paulo.\nO seu João fez uma pescaria e acabou pegando mais do que 50 quilos, a sua pesagem teve um execesso de {} Kg.\nPor ventura deste acontecimento ele terá que pagar uma multa que equivale a R$ 4,00 por quilo excedente. A multa ficaria em torno de R$ {:.2f}.'.format (excessoPeixe, multa))
else:
  print('Não teve excesso!')  


