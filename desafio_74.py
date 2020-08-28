# Crie um programa de 5 números aleatórios e coloque em uma tupla . Após isso :
# mostre os números gerados :
# mostre o menor e o maior número da tupla :

from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'\nOs números sorteados foram: {n}')
print(f'\nO maior número sorteado foi : {max(n)}')
print(f'\nO menor número sorteado foi : {min(n)}')





