# FAÇA UM PROGRAMA ONDE O COMPUTADOR JOGUE JOKENPÔ ( PEDRA, PAPEL E TESOURA) COM O USUÁRIO .
# As regras são as seguintes:
# Pedra empata com Pedra e ganha de Tesoura.
# Tesoura empata com Tesoura e ganha de Papel.
# Papel empata com Papel e ganha de Pedra

from random import randint
print('Vamos jogar Jokenpô ? ')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(' [0] Pedra\n [1] Papel\n [2] Tesoura')
jogador = int(input('Informe a sua jogada : '))
print(f'Eu já escolhi a minha opção:{itens[computador]}, você escolheu {itens[jogador]}')
if computador == 0 and jogador == 0:
    print('Empatamos ')
elif computador == 0 and jogador == 1:
    print('Você ganhou , parabéns !!')
elif computador == 0 and jogador == 2:
    print('Eu ganhei !!')
elif computador == 1 and jogador == 0:
    print('Eu ganhei !!')
elif computador == 1 and jogador == 1:
    print('Empatamos ')
elif computador == 1 and jogador == 2:
    print('Você ganhou , parabéns !!')
elif computador == 2 and jogador == 0:
    print('Você ganhou , parabéns !!')
elif computador == 2 and jogador == 1:
    print('Eu ganhei !!')
elif computador == 2 and jogador == 2:
    print('Empatamos ')
