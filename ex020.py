from random import shuffle
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo Aluno: ')
n3 = input('Terceiro Aluno: ')
n4 = input('Quarto Aluno: ')
list = [n1, n2, n3, n4]
shuffle(list)
print('A apresentação será feita na seguinte ordem:{} '.format(list))
