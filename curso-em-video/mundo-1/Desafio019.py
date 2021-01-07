import random

a1 = input('Insira o nome do aluno: ')
a2 = input('Insira o nome do aluno: ')
a3 = input('Insira o nome do aluno: ')
a4 = input('Insira o nome do aluno: ')

lista = [a1, a2, a3, a4]

print('O aluno escolhido para apagar o quadro foi \n'
      '{}'.format(random.choice(lista)))