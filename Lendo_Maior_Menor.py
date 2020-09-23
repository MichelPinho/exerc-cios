# ESCREVA UM PROGRAMA QUE LEIA 2 NÚMEROS DO TECLADO, INFORME AO USUÁRIO A SEGUINTE MENSAGEM :
# O PRIMEIRO VALOR É MAIOR
# O SEGUNDO VALOR É MAIOR
# NÃO EXISTE VALOR MAIOR, TODOS SÃO IGUAIS
n1 = int(input('Informe o primeiro valor -> '))
n2 = int(input('Informe o segundo valor -> '))

if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}.')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}.')
else:
    print('Os números são iguais.')
