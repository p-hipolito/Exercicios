min=0
max=0
for c in range(0,5):
    peso=float(input('Qual o seu peso? '))
    if c==0:
        min=peso
        max=peso
    else:
        if peso>max:
            max=peso
        elif peso<min:
            min=peso
print('O menor valor é {} e o maior é {}.' .format(min,max))