from random import randint
from time import sleep
conteudo=['Pedra','Papel','Tesoura']
jooj=randint(0,2)
jogador=int(input('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura
Qual sua escolha? '''))
print(conteudo[jooj])
if jooj==jogador:
    print('Empata n princesa, vai deixar a coroa cair.')
elif jooj==0:
    if jogador==1:
        print('Você ganhou.')
    else:
        print('Você perdeu.')
elif jooj==1:
    if jogador==0:
        print('Você perdeu.')
    else:
        print('Ocê ganhô.')
elif jooj==2:
    if jogador==0:
        print('Cê mim ganho deu.')
    else:
        print('Ti ganhei.')
else:
    print('escolhe uma opção vadiaputa.')
