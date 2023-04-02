n=cont=1
while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    cont=1
    if n<0:
        break
    while cont<11:
        print('{} x {} = {}' .format(n,cont,n*cont))
        cont+=1