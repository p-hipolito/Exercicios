alt=float(input('Qual a sua altura? '))
peso=float(input('Qual o seu peso? '))
imc=peso/alt**2
print('O seu IMC é de {:.1f}.' .format(imc))
if imc<18.5:
    print('Aidético do caralho')
elif imc<=25:
    print('Deixa o shape falar')
elif imc<=30:
    print('GORDOLA GORDOLA GORDOLA')
elif imc<=40:
    print('toma no teu cu ricardo')
else:
    print('já tá cm o pé na cova')