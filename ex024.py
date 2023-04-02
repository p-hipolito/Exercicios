cid = input('Em que cidade você mora? ').strip()
dec = cid.split()
print(cid[:5].upper() == 'SANTO')
if(dec[0].upper() == 'SANTO'):
    print('Cago-se?')
else:
    print('Podia ser pior né...')
    