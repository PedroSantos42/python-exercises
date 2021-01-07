n = int(input('Insira um número: '))

if n != 0:
    print('Número {} é par'.format(n) if (0 == n%2)
      else 'Número é ímpar')
else:
    print('Número inválido')