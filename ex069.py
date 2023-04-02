sexo=jef=''
demaior=homem=meninademenor=idade=0
while True:
    sexo=str(input('Qual seu sexo? [M]/[F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo=str(input('Qual seu sexo? [M]/[F]: ')).strip().upper()[0]
    idade=int(input('Qual a sua idade? '))
    jef=str(input('Deseja continuar? [S]/[N]: ')).strip().upper()[0]
    if idade>=18:
        demaior+=1
    if sexo=='M':
        homem+=1
    if sexo=='F' and idade<20:
        meninademenor+=1
    while jef not in 'SN':
        jef=str(input('Deseja continuar? [S]/[N]: ')).strip().upper()[0]
    if jef=='N':
        break
print('No total {} pessoas são maiores de idade.' .format(demaior))
print('No total {} pessoas são homens.' .format(homem))
print('No total {} garotas com menos de 20 anos.' .format(meninademenor))