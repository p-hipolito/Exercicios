num=int(input('Digite um valor: '))
jk='s'
soma=num
cont=0
min=num
max=num
while jk!='n':
    jk=str(input('Deseja continuar?[S]/[N]: ')).strip().lower()[0]
    if jk!='n':
        num=int(input('Digite outro número: '))
        if num>max:
            max=num
        elif min>num:
            min=num
    soma+=num
    cont+=1
print('A média entre todos os {} valores é {}.' .format(cont,soma/cont))
print('O menor valor é {}.'.format(min))
print('O maior valor é {}.'.format(max))