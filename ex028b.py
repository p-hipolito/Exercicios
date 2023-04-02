from random import randint
import colorama
from time import sleep
colorama.init()
x = randint(0,5) #Faz o Pc 'Pensar'
print(colorama.Fore.YELLOW + '-=-'*10)
print(colorama.Fore.CYAN + 'Vou pensar em um número entre 0 e 5.')
print(colorama.Fore.YELLOW + '-=-'*10)
y = int(input(colorama.Fore.CYAN + 'Tente advinhar: ')) #Acerta essa merda ae
print(colorama.Fore.YELLOW + 'PROCESSANDO...')
sleep(1)
if x==y:
    print(colorama.Fore.GREEN + 'PARABÉNS, você acertou!')
else:
    print(colorama.Fore.RED + 'ERROOOOU! Eu pensei no número {} e não em {}.' .format(x,y))