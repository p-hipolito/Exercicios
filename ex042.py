r1=int(input('Qual o tamanho da primeira reta? '))
r2=int(input('Qual o tamanho da segunda reta? '))
r3=int(input('Qual o tamanho da terceira reta? '))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    if r1==r2==r3:
        print('estas retas criam um triângulo equilátero.')
    elif r1!=r2 and r1!=r3 and r2!=r3:
        print('Triângulo escaleno, onde todos os lados são diferentes.')
    else:
        print('Triângulo isósceles, onde dois lados são iguais.')
else:
    print('Essas retas nem fodendo criam um triângulo.')