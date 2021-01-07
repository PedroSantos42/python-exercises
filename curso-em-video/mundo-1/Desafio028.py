import random

entrada = int(input('Insira o número entre 1 e 5: '))

numero = random.randint(1, 5)

if numero == entrada:
    print('Você venceu!')
else:
    print('Você perdeu!')

print('Valor inserido foi {} e o sorteado foi {}'.format(entrada, numero))