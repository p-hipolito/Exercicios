c=0
soma=0
jk=0
c=int(input('Digite um valor po pai: '))
while c!=999:
    jk+=1
    soma=soma+c
    c=int(input('Digite um valor po pai: '))
print('O valor total da soma entre os {} valores digitados é {}.'.format(jk,soma))