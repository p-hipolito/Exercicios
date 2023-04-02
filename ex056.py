velho=0
velho2=''
novinha=0
soma=0
for c in range(0,4):
    print('----- {}ª PESSOA -----' .format(c))
    nome= input('Digite seu nome: ')
    idade=int(input('Digite sua idade: '))
    sexo=input('Digite seu sexo[F ou M]: ')
    lista=[nome,idade,sexo]
    soma+=idade
    if sexo=='m' and idade>velho:
        velho=idade
        velho2=nome
    if sexo=='f' and idade<20:
        novinha+=1
print('A idade média do grupo é {:.0f}.'.format(soma/4))
print('O homem mais velho do grupo é o {}.'.format(velho2))
print('Neste grupo temos {} garotas com menos de 20 anos de idade.'.format(novinha))