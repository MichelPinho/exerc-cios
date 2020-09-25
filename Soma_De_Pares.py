# FAÇA UM PROGRAMA QUE LEIA 6 NÚMEROS INTEIROS, E MOSTRE A SOMA SOMENTE DOS NÚMEROS PARES.
# SE O VALOR FOI ÍMPAR, DESCONSIDERE-O.
soma = 0
for c in range(0, 6):
    num = int(input('Informe um número ->  '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos números pares são: {soma}')


