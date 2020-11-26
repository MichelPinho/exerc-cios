# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
listanum = []
menor = 0
maior = 0
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c} -> ')))
    if c == 0:
        menor = maior = listanum [c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print (f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {maior}, na posição',end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f' {i}...')
print(f'O menor valor digitado foi {menor}, na posição',end='')
# i = índice
for i, v in enumerate(listanum):
    if v == menor:
        print(f' {i}...')

