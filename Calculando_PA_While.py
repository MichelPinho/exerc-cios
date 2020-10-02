# REFAÇA O EXERCÍCIO DE CALCULAR UMA PA COM WHILE:
primeiro = int(input('Informe o primeiro termo da razão de uma P.A. ->  '))
razao = int(input('Informe a razão dessa P.A. ->  '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos você quer mostrar mais ?'))
print(f'\033[32mProgressão finalizada com sucesso, foram utilizados {total} termos neste exercício.')
print('FIM')
