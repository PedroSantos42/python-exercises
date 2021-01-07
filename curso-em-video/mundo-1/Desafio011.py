larg = float(input('Insira o valor da largura: '))
alt = float(input('Insira o valor da altura: '))

area = larg*alt
tinta = area/2

print('É necessário {:.2f} litros de tinta para pintar a parede'.format(tinta))