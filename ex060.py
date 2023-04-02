from math import factorial
num=int(input('Digite um número: '))
fat=num
res=1
#print(factorial(num)) -> Facilitador de vida
print('Calculando {}! = '.format(num))
while fat>0:
    print('{} '.format(fat), end='')
    print(' x ' if fat>1 else ' = ', end='')
    res*=fat
    fat-=1
print('O fatorial de {} é {}.'.format(num,res))