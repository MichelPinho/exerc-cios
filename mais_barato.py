#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

a = float(input(' Informe o primeiro preço: '))
b = float(input(' Informe o segundo preço: '))
c = float(input(' Informe o terceiro preço: '))

menor = a
## verificando o mais barato

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

print(f' O mais barato é R${menor:.2f}.')

