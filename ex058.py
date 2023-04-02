from random import randint
from time import sleep
tent=1
pc=randint(0,10)
player=int(input('Advinhe um número, de 0 a 10: '))
while pc!=player:
    if pc>player:
        player=int(input('Tenta de novo, um pouco maior: '))
    else:
        player=int(input('Tenta de novo, um pouco menor: '))
    tent+=1
print('Parabéns! Você acertou em {} tentativas!' .format(tent))