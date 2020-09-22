# ESCREVA UM PROGRAMA ONDE O COMPUTADOR "PENSE" EM UM NÚMERO DE 0 A 5
# E QUE O USUÁRIO TENTE ACERTAR O NÚMERO ESCOLHIDO PELO COMPUTADOR
# E MOSTRE NA TELA SE ELE ACERTOU OU ERROU

from random import randint
computador = randint(0, 5)
print('=-=' * 40)
usuario = int(input('Já pensei em um número, será que acertou ? escreva o seu número aqui ao lado ->'))
print('=-=' * 40)
print('O número que eu escolhi foi {}'. format(computador))
if computador == usuario:
    print("Acertou, parabéns !!!")
else:
    print('Você errou, eu ganhei')






