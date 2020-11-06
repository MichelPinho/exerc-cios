## Crie um programa que leia vários números inteiros pelo teclado.
## No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
## O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

media = quant = soma = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    quant += 1
    if quant == 1: 
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar ?[S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números,e sua média foi {}.'.format(quant, media))
print('O maior valor foi de {}, e o menor foi de {}.'.format(maior, menor))

