#Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

x = int(input('Digite um número de 1 à 7 , referente aos dias da semana: '))

if x == 1:
    print('Domingo')

elif x == 2:
    print('Segunda')

elif x == 3:
    print('Terça')

elif x == 4:
    print('Quarta')

elif x == 5:
    print('Quinta')

elif x == 6:
    print('Sexta')

elif x == 7:
    print('Sábado')

else:
    print('Valor inválido, repita a operação')
