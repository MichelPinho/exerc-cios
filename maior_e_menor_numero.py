#	Faça um Programa que leia três números e mostre o maior e o menor deles.


a = int(input(' Informe o primeiro número: '))
b = int(input(' Informe o segundo número: '))
c = int(input(' Informe o terceiro número: '))

menor = a
## verificando o menor numero

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

## verificando o maior numero
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f' O maior número é {maior}, e o menor número é {menor}.')
