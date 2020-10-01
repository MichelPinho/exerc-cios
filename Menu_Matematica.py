# CRIE UM PROGRAMA ONDE LEIA 2 NÚMEROS:
# CRIE UM MENU QUE TENHA :
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS
# [5] SAIR
# O SEU PROGRAMA DEVERÁ REALIZAR CADA OPERAÇÃO QUE O USUÁRIO ESCOLHER.
a = int(input('Digite o primeiro número : '))
b = int(input('Digite o segundo número: '))
menu = 0
while menu != 5:
    print(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos Números\n [5] Sair\n')
    menu = int(input('Escolha a opção do menu acima:'))
    if menu == 1:
        soma = a + b
        print(f'A soma de {a} + {b} é {soma}\n')
    elif menu == 2:
        mult = a * b
        print(f'Os números {a} x {b} é {mult}\n')
    elif menu == 3:
        maior1 = a > b
        maior2 = b > a
        if a > b:
            print(f'O maior número é {a}\n')
        else:
            print(f'O maior número é {b}\n')
    elif menu == 4:
        a = int(input('Escolha a primeira opção : '))
        b = int(input('Escolha a segunda opção: '))
        print(' [1] Somar\n [2] Multiplicar\n [3] Maior\n [4] Novos Números\n [5] Sair\n')
        menu = int(input('Escolha a opção do menu acima:'))
        if menu == 1:
            soma = a + b
            print(f'A soma de {a} + {b} é {soma}\n')
        if menu == 2:
            mult = a * b
            print(f'Os números {a} x {b} é {mult}\n')
        if menu == 3:
            maior1 = a > b
            maior2 = b > a
            if a > b:
                print(f'O maior número é {a}\n')
            else:
                print(f'O maior número é {b}\n')
        elif menu == 5:
            print('Saindo ...\n')
        else:
            print('Opção inválida, repita a operação.\n')
    elif menu == 5:
        print('Saindo ...\n')
    else:
        print('Opção inválida, repita a operação.\n')
print('Obrigado !')
