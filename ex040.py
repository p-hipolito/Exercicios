n1=int(input('Que nota você tirou na primeira avaliação? '))
n2=int(input('Que nota você tirou na segunda avaliação? '))
media=(n1+n2)/2
if media<5:
    print('Você deveria reconsiderar colocar esse resto de aborto na AACD.')
elif media==5:
    print('Olha, tá quase bom, mas ainda vai pra recuperação.')
else:
    print('Não faz mais que o mínimo.')