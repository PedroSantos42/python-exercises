r1 = float(input('Insira o valor da reta 1: '))
r2 = float(input('Insira o valor da reta 2: '))
r3 = float(input('Insira o valor da reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
