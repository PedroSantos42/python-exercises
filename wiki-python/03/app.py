# Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
# a velocidade de um link de Internet (em Mbps), 

# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

fileSize = float(input('Insira o tamanho do arquivo (em MB): '))

internetBandwith = float(input('Insira a velocidade da sua conexão (em Mbps): '))

timeToDownloadFile = int((fileSize * 8) / internetBandwith)

print(f'O tempo aproximado para download do arquivo é de {timeToDownloadFile} minutos')