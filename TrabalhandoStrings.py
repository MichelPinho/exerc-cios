#NOME COMPLETO DE UMA PESSOA
# NOME COM TODAS AS LETRAS MAIÚSCULAS
# NOME COM TODAS AS LETRAS MINÚSCULAS
# QUANTAS LETRAS AO TODOS, SEM CONSIDERAR OS ESPAÇOS
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input('Digite seu nome completo:')).strip()

nome.upper()
print(f'Seu nome completo com tudo maiusculo é: {nome.upper()}\nNome completo com tudo minúsculo é: {nome.lower()}')
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro é {} e tem {} letras'.format(separa[0], len(separa[0])))
