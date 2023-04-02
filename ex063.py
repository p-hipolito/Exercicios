inic=0
num=1
fib=int(input('Quantos números desta sequência gostaria de ver: '))
cont=3
print('{} -> {} -> '.format(inic,num), end='')
while cont<=fib:
    t3=inic+num
    print('{} '.format(t3), end='-> ')
    inic=num
    num=t3
    cont+=1
print('Final.')