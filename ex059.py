num1=int(input('Digite o primeiro valor: '))
num2=int(input('Digite o segundo valor: '))
opcao=0
while opcao!=5:
    opcao=int(input('''
ESCOLHA UMA OPÇÃO:
        [1] - SOMAR AMBOS OS NÚMEROS
        [2] - MULTIPLICAR OS NÚMEROS
        [3] - MAIOR ENTRE AMBOS
        [4] - ESCOLHER NOVOS NÚMEROS
        [5] - FECHAR A APLICAÇÃO
''' ))
    if opcao==0 or opcao>5:
        opcao=int(input('''ESCOLHA UMA OPÇÃO VÁLIDA:
        [1] - SOMAR AMBOS OS NÚMEROS
        [2] - MULTIPLICAR OS NÚMEROS
        [3] - MAIOR ENTRE AMBOS
        [4] - ESCOLHER NOVOS NÚMEROS
        [5] - FECHAR A APLICAÇÃO
        Sua escolha: '''))
    elif opcao==1:
        print('A soma entre {} e {} é {}.'.format(num1,num2,num1+num2))       
    elif opcao==2:
        print('A multiplicação entre {} e {} é {}'.format(num1,num2,num1*num2))
    elif opcao==3:
        if num1>num2:
            print('O maior valor é {}.'.format(num1))
        else:
            print('O maior valor entre ambos é {}.'.format(num2))
    else:
        num1=int(input('Digite o primeiro valor: '))
        num2=int(input('Digite o segundo valor: '))
    print('~=~'*10)
print('Aplicação encerrada.')