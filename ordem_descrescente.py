#	Faça um Programa que leia três números e mostre-os em ordem decrescente.

a = int(input(' Informe o primeiro número: '))
b = int(input(' Informe o segundo número: '))
c = int(input(' Informe o terceiro número: '))


## verificando a ordem decrescente

if a > b > c:
    print(a, b, c)
if a > c > b:
    print(a, c, b)
if b > a > c:
    print(b, a, c)
if b > c > a:
    print(b, c, a)
if c > a > b:
    print(c, a, b)
if c > b > a:
    print(c, b, a)
if a == b or b == c or c == a:
    print(' Existem núemros iguais, favor, refaça a operação.')
