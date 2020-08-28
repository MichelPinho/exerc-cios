# Desenvolva um programa que leia 4 números pelo teclado, e guarde-os em uma tupla, no final disso, mostre :
# Quantas vezes apareceu o número 9 ?
# Em que posição foi digitado o primeiro número 3 ?
# Quais são os números pares ?
n = (int(input('Digite um número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceiro número: ')), int(input('Digite o último número: ')))

print(f'Você digitou os valores: {n}')
# contando quantas vezes aparece o número 9:
print(f'\n O número 9 apareceu {n.count(9)} vezes')
# em que posição foi digitado o número 3:
if 3 in n:
    print(f'\n O número 3 foi digitado na {n.index(3)} posição')
else:
    print(' O número 3 não foi digitado')
# verificando se algum número digitado é par :

for n in n:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram: {n}')



