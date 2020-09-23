# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E O USUÁRIO DEVERÁ ESCOLHER SUA BASE DE CONVERSÃO:
# 1 PARA BINÁRIO
# 2 OCTAL
# 3 HEXADECIMAL
n = int(input('Informe um valor : '))
print('Escreva uma das bases para conversão:\n'
      '[1] Binário\n'
      '[2] Octal\n'
      '[3] Hexadecimal')
opcao = int(input('Selecione sua opção: '))
if opcao == 1:
    print(f'O número {n} convertido para Binário é {bin(n)[2:]}')
elif opcao == 2:
    print(f'O número {n} convertido para Octal é {oct(n)[2:]}')
elif opcao == 3:
    print(f'O número {n} convertido para Hexadecimal é {hex(n)[2:]}')
else:
    print('O número que você escolheu não é válido. Repita a operação')



