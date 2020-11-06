# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = soma = 0
num = int(input('Digite um valor [ o número 999 encerra a operação]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um valor [ o número 999 encerra a operação]: '))
print('Você digitou {} números e a soma deles é {}.'.format(cont, soma))
