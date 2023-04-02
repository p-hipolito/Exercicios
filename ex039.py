from datetime import date
nasc = int(input('Em que ano você nasceu?'))
dif=date.today().year-nasc
if dif==18:
    print('Você tem que se apresentar no quartel ainda hoje moleque.')
elif dif<18:
    print('Você vai ter que se alistar em {} anos.' .format(18-dif))
else:
    print('Já faz uns {} anos que você se apresentou.' .format(dif-18))