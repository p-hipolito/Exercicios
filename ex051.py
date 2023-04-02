termo=int(input('Qual o primeiro termo desta Progressão Aritmética? '))
razao=int(input('Qual a razão desta Progressão Aritmética? '))
decimo=termo+(10-1)*razao
for c in range (termo,decimo+razao,razao):
    print('{} '.format(c) , end='-> ')
print('CABÔ-SE')