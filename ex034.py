sal = float(input('Qual o seu salário? '))
if sal>1250.00:
    print('Seu salário atualizado, com o aumento de 10%, é R${:.2f}.' .format(sal+(sal*10/100)))
else:
    print('Seu salário atualizado, com o aumento de 15%, é R${:.2f}.' .format(sal+(sal*15/100)))