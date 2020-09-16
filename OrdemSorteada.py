#COLOCANDO ALEATÓRIAMENTE OS NOMES DOS ALUNOS
# UTILIZANDO O IMPORT RANDOM, COM O MÉTODO SHUFFLE ( EMBARALHADOR).

from random import shuffle
aluno1 = str(input('Digite o nome aluno(a):'))
aluno2 = str(input('Digite o nome aluno(a):'))
aluno3 = str(input('Digite o nome aluno(a):'))
aluno4 = str(input('Digite o nome aluno(a):'))
aluno5 = str(input('Digite o nome aluno(a):'))

lista1 = [aluno1, aluno2, aluno3, aluno4, aluno5]

shuffle(lista1)

print(f'O aluno sorteado foi: {lista1}')
