# ESCREVA UM PROGRAMA QUE RECEBA A VELOCIDADE DE UM CARRO , SE ELE ULTRAPASSAR 80 KM/H.
# INFORME QUE ELE FOI MULTADO.
# O VALOR DA MULTA É DE R$ 7,00 POR KM ACIMA DO LIMITE.

velFinal = int(input('Informe a velocidade do carro : '))
multa = (velFinal - 80) * 7

if velFinal <= 80:
    print('Parabéns, você está dentro dos limites de velocidade.')
else:
    print(f'Você não está dentro dos limites de velocidade e precisará pagar uma multa de R$ {multa:.2f}.')
