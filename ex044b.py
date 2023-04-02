print('{:=^40}'.format(' LOJAS TABAJARA '))
preço = float(input('Qual o preço normal do produto? '))
forma_pagamento = str(input("""Formas de pagamento:
[ 1 ] À vista: dinheiro ou cheque - 10% desc.
[ 2 ] À vista: cartão - 5% desc.
[ 3 ] 2X: cartão - preço normal
[ 4 ] 3X ou mais: cartão - 20% de juros
 Escolha uma das opções acima: """))
if forma_pagamento == "1":
    print('O produto terá um desconto de 10% e custará R$ {}{:.2f}'.format('\033[33m', preço * 0.9))
elif forma_pagamento == '2':
    print('O produto terá um desconto de 5% e custará R$ {}{:.2f}'.format('\033[33m', preço * 0.95))
elif forma_pagamento == '3':
    print('O cliente pagará o preço normal do produto: R$ {:.2f}, '.format(preço),end="")
    print('dividido em \033[35mduas parcelas de {:.2f}\033[m'.format(preço / 2))
elif forma_pagamento == '4':
    print('Nesse caso o produto terá um \033[31macréscimo de 20%\033[m e sairá por R$ {:.2f},'.format(preço * 1.20), end="")
    print(' dividido em 3 parcelas de {:.2f}'.format((preço * 1.2) / 3))
elif forma_pagamento != "1" != "2" != "3" != "4":
    print('\033[31mForma de pagamento inválida!')