n = str(input('Insira o nome completo: ')).strip().split()

ultimo = n[len(n)-1]
primeiro = n[0]

print('Primeiro nome: {} \n'
      'Último nome:   {}'.format(primeiro, ultimo))
