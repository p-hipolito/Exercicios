n1 = int(input('Quanto tirou na primeira prova? '))
n2 = int(input('Qual foi sua nota na segunda avaliação? '))
m = (n1+n2)/2
print('Sua média é de {},' .format(m) , end=' ')
if(m>=7):
    print('meus parabéns, você está aprovado!')
else:
    print('te vejo no ano que vem!')