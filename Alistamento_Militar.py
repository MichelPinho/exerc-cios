# FAÇA UM PROGRAMA QUE LEIA A DATA DE NASCIMENTO DO USUÁRIO E INFORME A SUA IDADE E DIGA :
# SE ELE PRECISA SE ALISTAR
# SE É HORA DE SE ALISTAR
# SE JÁ PASSOU DA HORA DO SEU ALISTAMENTO
# O SEU PROGRAMA DEVERÁ INFORMAR QUANTO TEMPO FALTA PARA SE ALISTAR, E SE JÁ PASSOU, QUANTO TEMPO JÁ PASSOU DO PRAZO
from datetime import date
print('=-=' * 40)
print('                                         ALISTAMENTO MILITAR                           ')
print('=-=' * 40)
no = str(input('Informe seu nome -> ')).strip()
na = int(input('Informe o ano de seu nascimento -> '))
hoje = date.today() # informa a data do seu computador
ano = hoje.year # puxa somente o ano do seu computador
idade = ano - na
pdata = idade - 18
fdata = 18 - idade
if idade < 18:
    print(f'Sr. {no} você tem {idade} anos, faltam {fdata} anos para o alistamento obrigatório.')
elif idade == 18:
    print(f'Sr. {no}, já pode servir a pátria !!.')
else:
    print(f'Sr. {no} , sua idade é {idade} anos, seu alistamento está atrasado {pdata} anos.')









