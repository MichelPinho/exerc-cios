# Faça um programa que leia 5 números e guarde em uma lista :
# Mostre qual o valor maior e o valor menor :
# Mostre o valor e suas respectivas posições :

lista= list()
maior = 0
menor = 0

for c in range(0, 5):
    lista.append(int(input(f' Digite um número para a posição {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('=-' * 30)
print(f' Os números escolhidos em ordem numérica são: {sorted(lista)}')

print('=-' * 30)
print(f' O maior número da lista é : {maior}')
print(f' O menor número da lista é : {menor}')

print('=-' * 30)
for p, n in enumerate(lista):
    print(f' Na posição {p} encontramos o valor {n}')

