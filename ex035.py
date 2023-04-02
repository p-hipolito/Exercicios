l1 = int(input('Digite o comprimento do primeiro lado: '))
l2 = int(input('Digite o comprimento do segundo lado: '))
l3 = int(input('Digite o comprimento do terceiro lado: '))
if (l1+l2>l3) and (l1+l3>l2) and (l2+l3>l1):
    print('Naicer, dá pra fazer um trigas.')
else:
    print('Tenta de novo aê resto de aborto.')