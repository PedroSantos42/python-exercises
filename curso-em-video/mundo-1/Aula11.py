
# \033[0;33;44m
#
# 0,1,4,7
# 30 - 37
# 40 - 47

# modulo colorize

print('\033[30;47mTeste\033[m')

print('\033[7;30;47mTeste\033[m')

a = 3
b = 5

print('Os valores são \033[30;47m{}\033[m e \033[7;30;47m{}\033[m'.format(a, b))

print('Os valores são {}{}{} e {}{}{}'.format('\033[30;47m', a, '\033[m', '\033[7;30;47m', b, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}

print('Os valores são {}{}{} e {}{}{}'.format(cores['azul'], a, cores['limpa'],
                                              cores['amarelo'], b, cores['limpa']))