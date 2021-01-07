# Faça um Programa para uma loja de tintas. 

# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 

# Considere que a cobertura da tinta é 
# de 1 litro para cada 6 metros quadrados 

# e que a tinta é vendida 
# em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;

# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

paintingArea = float(input('Insira a área que deverá ser pintada em m²: '))

paintGallons = ['galões', 18, 80]

paintCans = ['latas', 3.6, 25]

isPaintCansEnough = paintingArea <= 97.1

if isPaintCansEnough:
    print(f'Você deve comprar apenas {paintCans[0]} de {paintCans[1]} litros')
else:
    print(f'Você deve comprar apenas {paintGallons[0]} de {paintGallons[1]} litros')