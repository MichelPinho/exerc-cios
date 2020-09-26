# FAÇA UM PROGRAMA QUE LEIA A IDADE, NOME E SEXO DE 4 PESSOAS, NO FINAL MOSTRE:
# 1 - A MÉDIA DA IDADE DO GRUPO
# 2 - QUAL É O NOME DO HOMEM MAIS VELHO
# 3 - QUANTAS MULHERES TEM MENOS DE 20 ANOS.
soma = 0
media = 0
maioridadehomem = 0
nomevelho = 0
for p in range(1, 5):
    nome = str(input('Informe seu nome: ')).strip()
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe seu sexo [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

media = soma / 4
print(f'A media é {media}')
print(f'O homem mais velho se chama {nomevelho} e tem {maioridadehomem} anos.')
