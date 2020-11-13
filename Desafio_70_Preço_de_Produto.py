# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar ou não. No final, mostre:
# qual é o total gasto na compra.
# quantos produtos custam mais de R$1000.
# qual é o nome do produto mais barato.

totmil = preço = soma = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    soma += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
   
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
        
print(f'Foram comprados {totmil} unidades acima de R$ 1.000,00.')
print(f'A soma dos produtos são R$ {soma:.2f}')
print(f'O produto mais barato é {barato} e o preço é R$ {menor}')

