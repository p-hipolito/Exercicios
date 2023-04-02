dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Kms foram rodados?'))
print('O valor total do aluguel é de R${:.2f}!' .format(dia*60 + km*0.15))