##João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
## Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
## deve pagar uma multa de R$ 4,00 por quilo excedente.
## João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
## Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
## Imprima os dados do programa com as mensagens adequadas.

peso = int(input(' Digite aqui o peso de hoje : '))


if peso > 50:
    excedente = (peso - 50)
    peso_taxado = (peso - 50) * 4
    print(f'O seu Excesso foi de {excedente} Kg, precisará ser taxado.')
    print(f'O que você deverá pagar pela sua pesca hoje é : R$ {peso_taxado},00.')

elif peso < 50:
    print(f' Hoje você não deverá pagar nada .')
