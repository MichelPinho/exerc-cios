# REFAÇA O EXERCÍCIO DE CALCULAR UMA PA COM WHILE:
primeiro = int(input('Informe o primeiro termo da razão de uma P.A. ->  '))
razao = int(input('Informe a razão dessa P.A. ->  '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
