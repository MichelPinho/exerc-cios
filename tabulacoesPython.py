# Crie um programa que tenha várias palavras dentro de uma tupla ( sem acentos ) , após isso
# você deve mostrar para cada palavra quais são suas vogais :
objetos = ('CANETA', 1.20, 'LAPIS', 0.75, 'BORRACHA', 0.65, 'HIDROCOR', 1.95, 'A4', 18.50, 'APONTADOR', 0.25)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(objetos)):
    if pos % 2 == 0:
        print(f'{objetos[pos]:.<20}', end='')
    else:
        print(f'R${objetos[pos]:>7.2f}')


