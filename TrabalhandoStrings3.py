# ESCREVA O NOME DE UMA PESSOA E :
# MOSTRE O NOME COMPLETO :
# PRIMEIRO NOME :
# ÚLTIMO NOME :
n = str(input('Digite seu nome:')).upper().strip()
nome = n.split()
print('Olá, seja muito bem vindo.')
print('Seu nome completo é:{}'.format(n))
print('Seu primeiro nome é :{}'.format(nome[0]))
print('Seu último nome é :{}'.format(nome[len(nome) - 1]))
