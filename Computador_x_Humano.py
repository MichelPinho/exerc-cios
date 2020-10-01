# FAÇA UM PROGRAMA EM QUE O COMPUTADOR PENSE EM UM NÚMERO, O USUÁRIO PODERÁ DIGITAR NÚMEROS DE 1 A 10
# O USUÁRIO PODERÁ DIGITAR ATÉ ACERTAR, E MOSTRE NA TELA QUANTAS VEZES O USUÁRIO PRECISOU TENTAR PARA ACERTA O NÚMERO.

from random import randint

computador = randint(1, 10)
print('=-=' * 40)
print('Já pensei no meu número, agora, me diga o seu')
print('=-=' * 40)

acertou = False
contador = 0
while not acertou:
    pessoa = int(input('Qual número você acha que eu pensei ? -> '))
    contador += 1
    if computador == pessoa:
        acertou = True
print(f'Parabéns, eu pensei no número {computador}. Você acertou !!')
print(f'Legal o jogo, você precisou de {contador} chances para acertar. ')
