vCs = int('Insira o valor da casa: ')
sal = int('Insira o valor do salário: ')
n = int('Insira o tempo do pagamento: ')

prt = vCs / (n / 12)

if prt > (sal * 0,3): print('Venda não autorizada!')
else:
    print('O  valor da parcela é: {}'.format(prt))