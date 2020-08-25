# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:

#	Para homens: (72.7*h) - 58
#	Para mulheres: (62.1*h) - 44.7

sexo = int(input("Qual seu sexo ? (informe 1 para Homem, 2 para Mulher): "))

if sexo == 1:
    alt = float(input(' Digite aqui a sua altura em metros : '))
    peso_masculino = ((72.7 * alt) - 58)
    print(f'O seu peso ideal é : {peso_masculino}')

elif sexo == 2:
    alt = float(input(' Digite aqui a sua altura em metros : '))
    peso_feminino = ((62.1 * alt) - 44.7)
    print(f' O seu peso ideal é : {peso_feminino}')
