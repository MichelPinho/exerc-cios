# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações

print('\n                      ###    BEM VINDO    ### ')
usuario = str(input('\nDigite seu login :'))
senha = str(input('\n Digite sua senha :'))

while usuario == senha:
    print(' ERRO: a senha não pode ser o nome do usuário')
    usuario = str(input('\nDigite seu login :'))
    senha = str(input('\n Digite sua senha :'))

else:
    print(' Senha gravada com sucesso !!')
