# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

v = 0
while True:
    jogador = int(input('Escolha um número inteiro: '))
    computador = (randint(0, 10))
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Escolha par ou ímpar [P/I]')).strip().upper()[0]
    total = jogador + computador
    print(f'Você jogou {jogador} o eu joguei {computador}, total de {total} ', end= '' )
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if opcao == 'P':
        if total % 2 == 0:
            print('Você ganhou.')
            v += 1
        else:
            print('Você perdeu . kkkkk')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Você ganhou.')
            v += 1
        else:
            print('Você perdeu . kkkkk')
            break
    print('Vamos jogar de novo, quero ver se me ganha agora. kkkk')        
print(f'FIM DE JOGO. Você ganhou {v} vez(es).')

