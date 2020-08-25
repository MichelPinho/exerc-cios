#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
# continue pedindo até que o usuário informe um valor válido.

num = int(input('Digite um número de 0 à 10: '))

if num > 0:
    if num < 11:
        print(f' O seu número é: {num}')
    else:
        print('Repita a operação, pois esse número não é válido')
