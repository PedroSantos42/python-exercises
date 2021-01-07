v = int(input('Insira a velocidade do carro: '))

print('Você foi multado em {} reais'.format((v-80)*7) if v > 80
      else 'Não há multas')