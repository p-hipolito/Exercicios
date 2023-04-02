from math import sin,cos,tan,radians
ang = float(input('Digite o ângulo que você deseja: '))
print('O ângulo {:.1f} tem o SENO de {:.2f}.' .format(ang, sin(radians(ang))))
print('O ângulo {:.1f} tem o COSSENO de {:.2f}.' .format(ang, cos(radians(ang))))
print('O ângulo {:.1f} tem a TANGENTE de {:.2f}.' .format(ang, tan(radians(ang))))