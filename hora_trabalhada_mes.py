#  Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#  e mostre o total do seu salário no referido mês.

num1 = float(input(' Digite quanto você ganha por hora : '))
num2 = int(input(' Digite quantas horas você trabalha por dia : '))
num3 = int(input(' Digite aqui, quantos dias você trabalhou nesse mês : '))

conv = float ((num1 * num2)* num3)

print(' O seu salário será de : R$ %s' % conv)
