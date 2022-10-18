'''
20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
a - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c - A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
mediaParcial = (nota1 + nota2 + nota3) / 3

if mediaParcial == 10:
    print('Aprovado com Distinção!\nPor ter tido uma média de {:.2f}'.format(mediaParcial))
elif mediaParcial >= 7:
    print('Aprovado por ter alcançado a média!\nMédia do aluno foi {:.2f}'.format(mediaParcial))
else:
    print('Reprovado por não ter alcançado a média!\nMédia do aluno foi {:.2f}'.format(mediaParcial))        