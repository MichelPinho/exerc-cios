# CRIE UM PROGRAMA QUE RECEBE UM NÚMERO, E DIGA SE ELE É PAR OU ÍMPAR

num = int(input('Informe o número que deseje saber se é par ou ímpar: '))

if num % 2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é ímprar'.format(num))
