# CRIE UM PROGRAMA QUE LEIA A DATA DE NASCIMENTO DE 7 PESSOAS .
# MOSTRE QUANTAS PESSOAS JÁ ATINGIRAM A MAIOR IDADE E QUANTAS NÃO SÃO.
# MAIOR IDADE 21 ANOS.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input('Em que ano você nasceu: '))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo, tivemos {totmaior} pessoas maiores de idade,\n'
      f'e {totmenor} pessoas menores de idade.')
