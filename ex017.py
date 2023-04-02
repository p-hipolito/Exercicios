from math import sqrt,hypot
cat1 = float(input('Comprimento do cateto oposto: '))
cat2 = float(input('Comprimento do cateto adjacente: '))
hip = sqrt(cat1**2 + cat2**2)
hip2 = (cat1**2 + cat2**2)**0.5
print('A hipotenusa é {:.2f}.' .format(hip))
print('A hipotenusa mede {:.2f}' .format(hypot(cat1, cat2)))
print('A hipotenusa é {:.2f}.' .format(hip2))