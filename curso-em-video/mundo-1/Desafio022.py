nome = str(input('Insira o nome do camarada: ')).strip()

print('Nome em maiúsculas é {} \n'
      'Nome em minúsculas é {}'.format(nome.upper(), nome.lower()))

print(len(nome.replace(' ', '')))
print('Primeiro nome é {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0])))