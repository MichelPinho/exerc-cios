##Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar 1-matutino ou 2-Vespertino ou 3- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

a = int(input(' Informe o turno que frequenta (1) manhã, (2) tarde ou (3) noite: '))

if a == 1:
    print('Bom dia')
else:
    if a == 2:
        print('Boa tarde')
    else:
        if a == 3:
            print('Boa noite')
        else:
            print(' Valor inválido, refaça a operação')
