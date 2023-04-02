n = int(input('digite um número: '))
print('Segue a tabuada de {}:' .format(n))
for c in range (1,11):
    print('{} x {} é igual a: {}.' .format(n,c,n*c))