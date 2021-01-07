n = str(input('Insira uma frase: ')).lower().strip()

print('A letra "a" aparece: {}x \n'
      'A primeira posição é {} \n'
      'A última posição é:  {}'.format(n.count('a'), (n.find('a')+1), (n.rfind('a')+1)))
