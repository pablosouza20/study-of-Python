-'''
8- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
produto1 = float(input('Primeiro produto: R$ '))
produto2 = float(input('Segundo produto: R$ '))
produto3 = float(input('Terceiro produto: R$ '))

if produto1 < produto2 and produto1 < produto3:
  print('Este produto que você deve comprar, pois é mais barato. R$ {:.2f}'.format(produto1))
elif produto2 < produto1 and produto2 < produto3:
  print('Este produto que você deve comprar, pois este produto é mais barato. R$ {:.2f}'.format(produto2))
else:
  print('Este produto está mais em conta para você. R$ {:.2f}'.format(produto3))    