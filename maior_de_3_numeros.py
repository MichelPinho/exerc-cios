#Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input(' Informe o primeiro número: '))
n2 = int(input(' Informe o segundo número: '))
n3 = int(input(' Informe o terceiro número: '))


if n1 > n2 > n3:
    print(f'{n1} é o maior número')

else:
    if n1 < n2 > n3:
        print(f'{n2} é o maior número ')

    else:
        print(f'{n3} é o maior número')

