dist = float((input('Insira a distância em Km: ')))

if dist < 200:
    print('O preço da viagem foi {:.2f} reais'.format(dist * 0.5))
else:
    print('O preço da viagem foi {:.2f} reais'.format(dist * 0.45))
