# A CONFEDERAÇÃO DE NATAÇÃO PRECISA SABER EM QUAL CATEGIRA AS CRIANÇAS SE ENQUADRAM, FAÇA UM PROGRAMA QUE
# LEIA A DATA DE NASCIMENTO E CLASSIFIQUE:
# ATÉ 9 ANOS: MIRIM
# ATÉ 14 ANOS: INFANTIL
# ATÉ 19 ANOS: JUNIOR
# ATÉ 20 ANOS: SENIOR
# ACIMA DISSO : MASTER
from datetime import date
n = int(input('Informe o ano de seu nascimento -> '))
hoje = date.today() # informa a data do seu computador
ano = hoje.year # informa somente o ano do seu computador
idade = ano - n
if idade <= 9:
    print('Você se enquadra na categoria MIRIM.')
elif 9 < idade <= 14:
    print('Você se enquadra na categoria INFANTIL')
elif 14 < idade <= 19:
    print('Você se enquadra na categoria SÊNIOR')
else:
    print('Você se enquadra na categoria MASTER')
