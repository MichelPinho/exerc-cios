# Crie um programa que tenha uma tupla completamente preenchida com uma contagem
# de 0 até 20.
# Seu programa deverá ler do teclado um número de ( 0 até 20 ) e mostrá-lo por extenso :

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input(' Digite um número de 0 à 20:'))
    if (num <= 0) or (num >= 20):
        print('\nERRO: Refaça a operação')

    else:
        break

print(f'\nO número que você escolheu foi o {contagem[num]}')




