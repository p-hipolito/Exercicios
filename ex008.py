m = int(input('Quantos metros tem esta parede? '))
print('Certo, a parede tem {:.0f} centímetros, ou ' .format(m*100) , end='')
print('{:.0f} milímetros.' .format(m*1000))