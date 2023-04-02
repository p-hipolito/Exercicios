num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro: '))
if num1>num2:
    print('O número {} é maior.' .format(num1))
elif num2>num1:
    print('O número {} é maior.' .format(num2))
else:
    print('Os números {} e {} são idênticos.' .format(num1, num2))