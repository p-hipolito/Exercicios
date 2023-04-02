import random
a = input('Primeiro Aluno: ')
b = input('Segundo Aluno: ')
c = input('Terceiro Aluno: ')
d = input('Quarto Aluno: ')
lista = [a,b,c,d]
print('O aluno escolhido é: ' , random.choice(lista))