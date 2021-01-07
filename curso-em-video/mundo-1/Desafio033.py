n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print('{} é maior que {} e {}'.format(n1, n2, n3))
    else:
        print('{} é maior que {} e {}'.format(n3, n1, n2))
else:
    if n2 > n3:
        print('{} é maior que {} e {}'.format(n2, n1, n3))
    else:
        print('{} é maior que {} e {}'.format(n3, n1, n2))