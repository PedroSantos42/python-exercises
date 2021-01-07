n = int(input('Insira um número entre 0 e 9999: '))


print('Unidade: {} \n'
      'Dezena:  {} \n'
      'Centena: {} \n'
      'Milhar:  {}'.format(n%10,
                           (n//10)%10,
                           (n//100)%10,
                           (n//1000)%10))