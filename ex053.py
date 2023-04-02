frase=input('Digite algo: ').lower().replace(' ','')
rev = frase[::-1]
print('O inverso de {} é {}.' .format(frase,rev))
if frase==rev:
    print('girafarigkkkkkkkkkkk')
else:
    print('Esta frase não é um palíndromo.')