# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, 

# cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. 

# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 

# Escreva um programa que peça 
# o tipo e a quantidade de carne comprada pelo usuário 

# e gere um cupom fiscal, contendo as informações da compra: 
# tipo e quantidade de carne, 
# preço total, 
# tipo de pagamento, 
# valor do desconto e 
# valor a pagar.

def calculateTotalPrice(quantity, selectedMeat):
    price = 0
    if quantity <= 5:
        if selectedMeat == 'File Duplo':
            price = quantity * 4.9
        elif selectedMeat == 'Alcatra':
            price = quantity * 5.9
        elif selectedMeat == 'Picanha':
            price = quantity * 6.9
    else:
        if selectedMeat == 'File Duplo':
            price = quantity * 5.8
        elif selectedMeat == 'Alcatra':
            price = quantity * 6.8
        elif selectedMeat == 'Picanha':
            price = quantity * 7.8

    return price


def calculateDescount(price, paymentMethod):
    if (paymentMethod.__contains__('Tabajara')):
        return price * 0.05
    else:
        return 0


print('O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:')
print('                      Até 5 Kg           Acima de 5 Kg')
print('File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg')
print('Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg')
print('Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg')

selectedMeat = input('Insira o nome carne desejada: ')
quantity = float(input('Insira a quantidade desejada (em Kg): '))

paymentMethod = input('Insira o método de pagamento: ')

totalPrice = calculateTotalPrice(quantity, selectedMeat)

descount = calculateDescount(totalPrice, paymentMethod)

priceWithDescount = totalPrice - descount

print(
    f'Pedido            : {quantity} Kg de {selectedMeat} \n'
    f'Preço total       : R$ {totalPrice:.2f} \n'
    f'Tipo de pagamento : {paymentMethod} \n'
    f'Valor do desconto : R$ {descount:.2f} \n'
    f'Valor do a pagar  : R$ {priceWithDescount:.2f} \n'
)
