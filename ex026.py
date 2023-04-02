hjk = input('Digite uma frase: ').strip()
print('Na frase a letra A aparece {} vezes.'.format(hjk.lower().count('a')))
print('A letra a aparece pela primeira vez na posição {}.'.format(hjk.lower().find('a')+1))
print('A letra a aparece pela última vez na posição {}.'.format(hjk.lower().rfind('a')+1))