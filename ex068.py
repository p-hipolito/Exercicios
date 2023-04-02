from random import randint
cont=pc=jogador=soma=0
player=''
print('~=~'*10)
print('Vamos jogar par ou impar!')
print('~=~'*10)
while True:
    jogador=int(input('Digite um número: '))
    pc=randint(0,9)
    soma=pc+jogador
    player=input('Par ou Ímpar? ').strip().lower()[0]
    if player=='p'and soma%2==0:
             print('Você jogou {} e eu joguei {}, o total de {} é PAR.' .format(jogador,pc,soma))
             cont+=1
             print('~=~'*10)
    elif player=='i' and soma%2==1:
          print('Você jogou {} e eu joguei {}, o total de {} é ÍMPAR.' .format(jogador,pc,soma))
          cont+=1
          print('~=~'*10)
    else:
          print('ERROU!')
          break
if soma%2==0:
      print('Você jogou {} e eu joguei {}, o total de {} é PAR.' .format(jogador,pc,soma))
else:
      print('Você jogou {} e eu joguei {}, o total de {} é ÍMPAR.' .format(jogador,pc,soma))
print('Você acertou {} vezes consecutivas.'.format(cont))