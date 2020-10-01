# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO E MOSTRE O SEU FATORIAL.
# EX: 5! = 5X4X3X2X1 = 120

from math import factorial
num = int(input('Informe o número para que eu possa calcular seu fatorial -> '))
calc = factorial(num)
contador = num
print('{}!='.format(num), end= '')
while contador > 1:
    contador -=  1
    print('{}'.format(contador), end='')
    print('x' if contador > 1 else '=', end='')
print(f'{calc}')
