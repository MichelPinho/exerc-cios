#SORTEANDO ALEATÓRIAMENTE UM NOME DE ALUNO
# UTILIZANDO O IMPORT RANDOM, COM O MÉTODO CHOICE ( ESCOLHA).

import random
aluno1 = str(input('Digite o nome aluno(a):'))
aluno2 = str(input('Digite o nome aluno(a):'))
aluno3 = str(input('Digite o nome aluno(a):'))
aluno4 = str(input('Digite o nome aluno(a):'))
aluno5 = str(input('Digite o nome aluno(a):'))

lista1 = [aluno1, aluno2, aluno3, aluno4, aluno5]

sorteio = random.choice(lista1)

print(f'O aluno sorteado foi: {sorteio}')

