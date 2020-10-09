num1 = int(input('Informe o primeiro número  -> '))
num2 = int(input('Informe o segundo número, ele deve ser menor que o primeiro -> '))
soma = 0
if num1 < num2:
    print('O segundo número digitado é maior que o primeiro, não pode, repita a operação.')
else:
    for c in range(num2, num1+1):
        soma += c
        print('{}'.format(c), end='')
        print('+' if c < num1 else '=', end='')
    print(soma)
print('Fim do programa.')

