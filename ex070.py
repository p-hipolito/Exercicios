fim=menor=produto=''
preço=total=topg=contagem=0
while True:
    produto=str(input('Produto: '))
    preço=float(input('Preço: R$'))
    if contagem==0 or contagem>preço:
        menor=produto
        contagem=preço
    if preço>=1000:
        topg+=1
    total+=preço
    fim=str(input('Deseja continuar? [S]/[N]: ')).strip().upper()[0]
    while fim not in 'SN':
        fim=str(input('Deseja continuar? [S]/[N]: ')).strip().upper()[0]
    if fim=='N':
        break
print('O preço total é de R${:.2f}.' .format(total))
print('O número de produtos com valor acima de R$1K é de {}.' .format(topg))
print('{} é o produto mais barato, com o valor de R${}.' .format(menor, contagem))