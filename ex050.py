p=0
cont=0
for c in range (0,6):
    num=int(input('Digite um número: '))
    if num%2==0:
        p+=num
        cont+=1
print('Você informou {} números pares e a soma total deles é {}.'.format(cont,p))
