#  Crie um programa que simule o funcionamento de um caixa eletrônico.
#  No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
# programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=-=' * 30)
print('BEM VINDO AO BANCO 24 HORAS')
print('=-=' * 30)

print('Este caixa possuí cédulas de R$100, R$50, R$20, R$10, R$2 e R$1')
valor = int(input('Informe o valor que deseja sacar -> '))
total = valor
totcedula = 0
cedula = 100

while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else :
        if totcedula > 0:
            print(f'O total de cédulas são {totcedula} e o valor sacado foi R$ {cedula}')
        if cedula == 100:
            cedula = 50
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
