n = str(input('Insira o nome da cidade: ')).strip().upper().split()

print('A cidade tem "Santo" no nome?')
print('SANTO' in n[0])