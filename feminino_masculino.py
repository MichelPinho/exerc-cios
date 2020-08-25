#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

acao = int(input(' Informe o seu sexo, 1 para M ou 2 para F :'))


if acao == 1:
    print('sexo MASCULINO')

else:
    if acao == 2:
        print(' sexo FEMININO')

    else:
        print('informação incorreta, repita a operação')

