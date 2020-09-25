# FAÇA UM PROGRAMA QUE LEIA O PESO DE 5 PESSOAS. DEPOIS DIGA QUEM TEM O MAIOR E O MENOR PESO.
#peso = float(input('Informe seu peso: '))
maior = 0
menor = 0

for p in range(1, 6):
    peso = (float(input(f'Informe o peso da {p}° pessoa :')))
    if p == 1:  # 1 pessoa - se o peso que foi dado é maio e menor já entram ness IF
        maior = peso
        menor = peso
    else: # se não entrar no IF de cima, pega esse de baixo, 2 pessoa.
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}Kg, e o menor é {menor}Kg.')
