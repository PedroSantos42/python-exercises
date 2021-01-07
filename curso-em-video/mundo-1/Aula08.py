from math import sqrt, ceil, floor
import random

#num = int(input('Insira o número: '))
num = random.randint(1, 100)
raiz = sqrt(num)

print('A raiz de {} é igual a   {:.2f} \n'
      'Arrendondada para cima:  {} \n'
      'Arrendondada para baixo: {}'.format(num, raiz, ceil(raiz), floor(raiz)))