# DIGITE UM NÚMERO DE 0 ATÉ 9999
# INFORME A UNIDADE, DEZENA CENTENA E MILHAR DESSE NÚMERO
# EX : 1998
# UNIDADE: 8
# DEZENA : 9
# CENTENA: 9
# MILHAR : 1

num = int(input('Informe um número inteiro de o até 9999: '))


unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f' A unidade é: {unidade}\n A dezena é: {dezena}\n A centena é: {centena}\n A milhar é: {milhar}')






