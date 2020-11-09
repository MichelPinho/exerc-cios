# Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


tothomens = totM20 = tot18 = 0
while True:
    idade = int(input('Informe a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu sexo [M/F] ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomens += 1 
    if sexo == 'F' and idade < 20:
        totM20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos são {tot18}.')
print(f'O total de homens cadastrados são {tothomens}.')
print(f'O total de mulheres com menos de 20 anos são {totM20}.')
