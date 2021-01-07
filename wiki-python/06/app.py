# Faça um programa que mostre os n termos da Série a seguir:

#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

# Imprima no final a soma da série.

numerator = int(input('Insira o valor do numerador: '))

denominator = int(input('Insira o valor do denominador: '))

n = 1
d = 1

# while (n < numerator or d < denominator):
while max(n, d) <= max(numerator, denominator):
    print(f'{n}/{d}')
    if n <= numerator:
        n = n + 1
    if d <= denominator:
        d = d + 1
