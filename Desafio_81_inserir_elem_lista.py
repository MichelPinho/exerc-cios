# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = list()
r = 0
while True:
    n = int(input('Digite um número -> '))
    numeros.append (n)
    r = str(input('Deseja continuar [S/N] ?'))
    if r in 'Ss':
        n = int(input('Digite um número -> '))
        numeros.append (n)
        r = str(input('Deseja continuar [S/N] ?'))
    else:     
        break
print(f'{numeros}')
