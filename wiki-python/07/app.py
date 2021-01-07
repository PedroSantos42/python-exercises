# Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

number = int(input('Insira um número: '))

outputNumber = number

for i in range(1, number):
    outputNumber = outputNumber + 1/number

print(f'O cálculo dos termos é {outputNumber:.2f}')
