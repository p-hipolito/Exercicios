termo=int(input('Digite o primeiro termo desta PA: '))
razao=int(input('Digite a razão desta PA: '))
zzz=10
print('Seguem os 10 primeiros termos da PA com termo inicial {} e razão {}:' .format(termo,razao))
while zzz!=0:
    termo+=razao
    zzz-=1
    print(termo,end=' -> ')
    if zzz==0:
        zzz=int(input('''
        Quantos termos a mais você quer ver? '''))
print('Final.')