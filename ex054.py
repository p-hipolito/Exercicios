from datetime import date
maior=0
men=0
ano=date.today().year
for c in range(0,7):
    nasc=int(input('Em que ano você nasceu? '))
    if ano-nasc>=18:
        maior+=1
    elif ano-nasc<18:
        men+=1
print('O total de pessoas maiores de idade neste grupo é: ',maior)
print('O total de pessoas menores de idade nesse grupo é:',men)