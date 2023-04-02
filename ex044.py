prod=float(input('Quanto custa o produto? '))
pagamento=input('Qual o método de pagamento? ').lower()
x=0
y=0
if pagamento=='dinheiro' or pagamento=='cheque':
    print('O valor final é de R${:.2f}.' .format(prod-(prod*10/100)))
else:
    x=input('Débito ou crédito? ').lower()
    if x=='crédito':
        y=int(input('Em quantas vezes? '))
        if y>=3:
            print('O valor final é de R${:.2f}.  Em {} parcelas de R${:.2f}.' .format(prod+(prod*20/100), y, (prod+prod*20/100)/y))
        else:
            print('O valor total é de R${:.2f}.' .format(prod))
    else:
        print('O valor final é de R${:.2f}.' .format(prod-prod*5/100))
    