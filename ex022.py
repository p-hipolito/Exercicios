name = input('Por favor digite seu nome completo: ').strip()
div = name.split()
print('Seu nome em letras maiúsculas é: ', name.upper())
print('Seu nome em letras minúsculas é: ', name.lower())
print('O comprimento total de seu nome é: ', len(name))
print('O comprimento total de seu nome sem espaços é: ', len(''.join(div)))
print('O comprimento total de seu primeiro nome é: ', len(div[0]))
print('O comprimento total de seu primeiro nome é: ', name.find(' '))
print('O comprimento total de seu nome sem espaços é: ', len(name.replace(' ', '' )))
print('O comprimento total de seu nome sem espaços é: ', len(name)-name.count(' '))