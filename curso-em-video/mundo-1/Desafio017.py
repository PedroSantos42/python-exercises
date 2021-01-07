from math import hypot, sqrt

c1 = float(input('Insira o valor do cateto oposto: '))
c2 = float(input('Insira o valor do cateto adjacente: '))

print('A hipotenusa do triângulo é: {:.2f}'.format(hypot(c1,c2)))

print('A hipotenusa do triângulo é: {:.2f}'.format(sqrt((c1**2 + c2**2))))