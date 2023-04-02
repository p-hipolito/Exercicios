num = int(input('Qual a distância que planeja viajar? '))
if num <= 200:
    print('A passagem custará R${}.' .format(num*0.50))
else:
    print('A passagem custará R${:.2f}.' .format(num*0.45))