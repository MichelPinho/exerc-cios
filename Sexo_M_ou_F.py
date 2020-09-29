# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA , M OU F
# CASO ESTEJA ERRADO, SOLICITE QUE DIGITE NOVAMENTE ATÉ ACERTAR.

sexo = str(input('Informe o seu sexo, [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação incorreta, favor escolher [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
