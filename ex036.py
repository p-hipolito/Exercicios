emp = float(input('Qual o valor do empréstimo que o senhor necessita? R$'))
prest = int(input('Por quantos anos o senhor pretende financiar? '))
salary = float(input('Por último, qual o seu salário? R$'))
emp = emp+emp*10/100
mens = emp/(prest*12)
if salary*30/100>=mens:
    print('O valor total será de R${:.2f}. \nO valor das parcelas será de R${:.2f}.\n O senhor gostaria de continuar?' .format(emp, mens))
else:  
    print('Infelizmente o senhor não atende aos requisitos para esta modalidade de financiamento.')