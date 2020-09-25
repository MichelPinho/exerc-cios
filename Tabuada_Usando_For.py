# FAÇA A TABUADA DE UM NÚMERO USANDO O FOR.
num = int(input('Informe qual número gostaria de saber a tabuada -> '))
for c in range(1, 11):
    resultado = num * c
    print(num, 'x', c, '=', resultado)
print('FIM')
