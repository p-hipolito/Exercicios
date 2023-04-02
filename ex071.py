num=int(input('Quanto gostaria de sacar? '))
nota100=nota50=nota20=nota1=0
while num>0:
    if num>0 and num%100==0:
        num-=100
        nota100+=1
    elif num>0 and num%50==0:
        num-=50
        nota50+=1
    elif num>0 and num%20==0:
        num-=20
        nota20+=1
    elif num>0 and num%1==0:
        num-=1
        nota1+=1
print(num)
if nota100>0:
    print(f'Total de {nota100} notas de R$100,00.')
if nota50>0:
    print(f'Total de {nota50} notas de R$50,00.')
if nota20>0:
    print(f'Total de {nota20} notas de R$20,00.')
if nota1>0:
    print(f'Total de {nota1} notas de R$1,00.')