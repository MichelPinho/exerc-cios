# Crie um programa que tenha várias palavras dentro de uma tupla ( sem acentos ) , após isso
# você deve mostrar para cada palavra quais são suas vogais :


letras = (str(input('Informe uma palavra para eu te dizer as vogais -> ')))

for p in letras:
    if p.lower() in 'aeiou':
        print(letras.upper() , end='')
        print(f' .As vogais são {p}')


