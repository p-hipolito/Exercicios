termo=int(input('Digite o primeiro termo desta PA: '))
razao=int(input('Digite a razão desta PA: '))
zzz=0
print('Seguem os 10 primeiros termos da PA com termo inicial {} e razão {}:' .format(termo,razao))
while zzz<10:
    print(termo,end=' -> ')
    termo+=razao
    zzz+=1
print('Final.')