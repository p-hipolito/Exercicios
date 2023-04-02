from random import randint
from time import sleep
x = randint(0,5) #Faz o Pc 'Pensar'
print('-=-'*10)
print('Vou pensar em um número entre 0 e 5.')
print('-=-'*10)
y = int(input('Tente advinhar: ')) #Acerta essa merda ae
while x<y:
        y = int(input('Tenta de novo, um pouco menor: '))
if x>y:
        y = int(input('Tenta de novo, um pouco maior: '))
print('Parabéns caralhoooou!')