# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Digte a PRIMEIRA nota do bimestre: '))
nota2 = float(input('Digite a SEGUNDA nota do bimestre: '))
nota3 = float(input('Digite a TERCEIRA nota do bimestre: '))
nota4 = float(input('Digite a QUARTA nota do bimestre: '))

print('Nota do primeiro bimestre: {}\nNota do segundo bimestre: {}\nNota do terceiro bimestre: {}\nNota do quarto bimestre: {}\nMédia final: {}'.format(nota1, nota2, nota3, nota4, (nota1+nota2+nota3+nota4)/4))