# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#	o produto do dobro do primeiro com metade do segundo .
#	a soma do triplo do primeiro com o terceiro.
#	o terceiro elevado ao cubo.

num1 = int(input(' Digite aqui um número inteiro : '))
num2 = int(input(' Digite aqui um número inteiro  : '))
num3 = float(input(' Digite aqui um número real : '))

conv1 = float ((num1 * 2) * (num2/2))
conv2 = int ((num1 * 3) + num3)
conv3 = float (num3 ** 3)
print(' O produto do dobro do primeiro com metade do segundo é : %s' % conv1)
print(' A soma do triplo do primeiro com o terceiro é : %s ' % conv2)
print(' O terceiro elevado ao cubo é : %s' % conv3)
