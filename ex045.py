import random
jooj=random.choice(['pedra', 'papel', 'tesoura'])
play=input('Pedra, papel ou tesoura? ').lower().strip()
if play==jooj:
    print('Empata n xerequinha')
elif jooj=='pedra' and play=='tesoura':
    print('Pedra ganha de tesoura. Ganhei otário!')
elif jooj=='pedra' and play=='papel':
    print('Papel ganha de pedra. Perdi... :c')
elif jooj=='papel' and play=='pedra':
    print('Papel ganha de pedra. PERDEU OTÁRIO!')
elif jooj=='papel' and play=='tesoura':
    print('Tesoura ganha de papel. Perdi... T^T')
elif jooj=='tesoura' and play=='papel':
    print('Tesoura ganha de papel. Ganhei, retardado!')
else:
    print('Pedra ganha de tesoura. Perdi uwu')