# 18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivoMB = float(input('Informe o tamanho do arquivo em megabytes para realizar o download: '))
veloInternet = int(input('Informe a sua velocidade do link de internet: '))
tempo = arquivoMB / veloInternet
minutos = tempo / 60
print('Tempo estimado do download: {:.2f} minutos.'.format(minutos))

