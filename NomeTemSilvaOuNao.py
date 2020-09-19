# ESCREVA O NOME DE UMA PESSOA E DIGA SE ELA TEM OU NÃO O " SILVA" NO SEU NOME

nome = str(input('Escreva seu nome completo : ')).strip()

x = 'silva' in nome.lower()
print(f'O seu nome é "{x}" Silva')


