# ESCREVA UMA FRASE QUALQUER E MOSTRE:
# QUANTAS VEZES APARECE A LETRA "a"
# EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ
# EM QUE POSIÇÃO ELA APARECE PELA ÚLTIMA VEZ

frase = str(input('Escreva uma frase qualquer:')).upper().strip()

print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A letra "A" apareceu na posição {}.'.format(frase.find('A') + 1))
print('A letra "A" apareceu pela última vez na posição {}.'.format(frase.rfind('A') + 1))







