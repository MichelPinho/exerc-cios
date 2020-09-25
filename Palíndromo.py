# FAÇA UM PROGRAMA QUE LEIA UMA FRASE E DIGA SE É UM PALÍNDROMO OU NÃO, DESCONSIDERANDO OS ESPAÇOS.
# POLÍNDROMO SÃO FRASES QUE PODEMOS LER DE TRÁS PARA A FRENTE E VICE-VERSA.
frase = str(input('Digite uma frase -> ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f' A palavra normal foi {junto}, seu inverso é {inverso}')
if inverso == junto:
    print('É PALÍNDROMO.')
else:
    print('NÃO É UM PALÍNDROMO.')
