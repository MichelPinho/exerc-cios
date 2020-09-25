# FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO INTEIRO E DIGA SE ELE É PRIMO OU NÃO.
#  REGRA : PARA SER CONSIDERADO NÚMERO PRIMO, ELE SÓ PODER DIVISÍVEL POR 1 E POR ELE MESMO.
num = int(input('Será que esse número é primo, vamos descobrir, me diga esse número -> '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
if tot == 2:
    print(f'\nO número {num} É PRIMO !!!')
else:
    print(f'\nO número {num} NÂO É PRIMO !!!')




