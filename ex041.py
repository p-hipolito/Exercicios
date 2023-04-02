from datetime import date
nasc = int(input('Em que ano você nasceu? '))
idade=date.today().year-nasc
if idade<=9:
    print('Você irá competir na categoria Mirim.')
elif idade<=14:
    print('Você irá competir na categoria Infantil.')
elif idade<=19:
    print('Você irá competir na categoria Junior.')
elif idade<=25:
    print('Você irá competir na categoria Senior.')
else:
    print('Você irá competir na categoria Master.')