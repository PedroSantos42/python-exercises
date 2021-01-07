sal = float(input('Insira o salário: '))

print('Aumento foi de {}'.format(sal * 0.1) if sal > 1250
      else 'Aumento foi de {}'.format(sal * 0.15))