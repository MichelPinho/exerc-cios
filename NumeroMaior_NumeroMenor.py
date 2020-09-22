# ESCREVA UM PROGRAMA QUE RECEBA 3 NÚMEROS, E INFORME QUAL É O MAIOR E QUAL É O MENOR
a = int(input('Escreva o primeiro número:'))
b = int(input('Escreva o segundo número:'))
c = int(input('Escreva o terceiro número:'))

if a > b > c:
    print('O maior número é {} e o menor número é {}.'.format(a, c))
elif a > c > b:
    print('O maior número é {} e o menor número é {}.'.format(a, b))
elif b > a > c:
    print('O maior número é {} e o menor número é {}.'.format(b, c))
elif b > c > a:
    print('O maior número é {} e o menor número é {}.'.format(b, a))
elif c > a > b:
    print('O maior número é {} e o menor número é {}.'.format(c, b))
else:
    print('O maior número é {} e o menor número é {}.'.format(c, a))
