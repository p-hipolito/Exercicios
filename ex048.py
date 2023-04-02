s=0
numero=0
for c in range(1,501,2):
    if c%3==0:
        print(c)
        s+=c
        numero+=1
print('A soma total dos {} números é: {}.'.format(numero,s))