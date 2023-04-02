temp = input('Que temperatura gostaria de converter? C/F: ')
if(temp == 'c'):
    c = float(input('Qual a temperatura atual? '))
    print('A temperatura atual é de {:.1f}°F!' .format(c*9/5+32))
else:
    f = float(input('Qual a temperatura atual? '))
    print('A temperatura atual é de {:.1f}°C!' .format(f/9*5-32))
