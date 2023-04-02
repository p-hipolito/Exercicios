
vel = int(input('A quantos Km/h você está andando? '))
if vel > 80:    
    print('Você será multado, a multa é de R${:.2f}.' .format((vel-80)*7))
else:
    print('Tenha um bom dia, dirija com segurança.')