# CALCULE UM PROGRAMA QUE LEIA UM ANO, E INFORME SE ELE É BISSEXTO OU NÃO
#No final do século XVI foi introduzido o calendário Gregoriano, usado até hoje na maioria dos países
# adotando as seguintes regras:
#1- Todo ano divisível por 4 é bissexto
#2- Todo ano divisível por 100 não é ano bissexto
#3- Mas se o ano for também divisível por 400 é ano bissexto

ano = int(input('Será que é ano Bissexto ? vamos descobrir, informe o ano -> '))

if ano % 4 == 0:
    print(f'O ano {ano} é Bissexto.')
elif ano % 100 == 0 and ano % 400 == 0:
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano}, não é Bissexto.')




