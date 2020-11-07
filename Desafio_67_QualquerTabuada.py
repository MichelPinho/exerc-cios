# Faça um programa que mostre a tabuada de vários números, um de cada vez,  
# para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

print('-=' * 50)
print('DESAFIO DA TABUADA')
print('-=' * 50)

while True:
    print('-' * 50)
    num = int(input('Quer ver a tabuada de qual valor [Número negativo encerra o programa]: '))
    print('-' * 50)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('Programa encerrado, volte sempre !!!')

