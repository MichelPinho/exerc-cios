#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#	Desconto do IR:
#	Salário Bruto até 900 (inclusive) - isento
#	Salário Bruto até 1500 (inclusive) - desconto de 5%
#	Salário Bruto até 2500 (inclusive) - desconto de 10%
#	Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#	        Salário Bruto: (5 * 220)        : R$ 1100,00
#	        (-) IR (5%)                     : R$   55,00
#	        (-) INSS ( 10%)                 : R$  110,00
#	        FGTS (11%)                      : R$  121,00
#	        Total de descontos              : R$  165,00
#       Salário Liquido                 : R$  935,00


num1 = float(input(' Digite quanto você ganha por hora : '))
num2 = int(input(' Digite quantas horas você trabalha por dia : '))
num3 = int(input(' Digite aqui, quantos dias você trabalhou nesse mês : '))


salario_bruto = float(num1 * num2 * num3)
inss = float(salario_bruto * 10/100)
ir1500 = float(salario_bruto * 5/100)
ir2500 = float(salario_bruto * 5/100)
ir = float(salario_bruto * 20/100)
sindicato = float(salario_bruto * 3/100)
fgts = float(salario_bruto * 11/100)
descontos = float(inss + sindicato + fgts)
descontos1500 = float(inss + sindicato + fgts + ir1500)
descontos2500 = float(inss + sindicato + fgts + ir2500)
descontos_acima = float(inss + sindicato + fgts + ir)
salario_liquido = float(salario_bruto - descontos)
salario_liquido1500 = float(salario_bruto - descontos1500)
salario_liquido2500 = float(salario_bruto - descontos2500)
salario_liquido_acima = float(salario_bruto - descontos_acima)

if salario_bruto <= 900:

    print(f' Seu salário bruto desse mês é : R${salario_bruto:.2f}')
    print(' Isento de Imposto de Renda')
    print(f' Você será descontado em 10% de INSS, o valor é de R$ {inss:.2f}')
    print(f' Você será descontado de 11% de FGTS, o valor é de R$ {fgts:.2f} ')
    print(f' Você será descontado em 3% do SINDICATO, o valor é de R$ {sindicato:.2f}')
    print(f' O total de descontos nesse mês será de : R${descontos:.2f}')
    print(f'Salário R${salario_bruto:.2f} menos os descontos R${descontos:.2f} terá líquido de R${salario_liquido:.2f}')

elif salario_bruto <= 1500:
    print(f' Seu salário bruto desse mês é : R${salario_bruto:.2f}')
    print(f' Você será descontado em 5% de IR, o valor é de R$ {ir1500:.2f}')
    print(f' Você será descontado em 10% de INSS, o valor é de R$ {inss:.2f}')
    print(f' Você será descontado de 11% de FGTS, o valor é de R$ {fgts:.2f} ')
    print(f' Você será descontado em 3% do SINDICATO, o valor é de R$ {sindicato:.2f}')
    print(f' O total de descontos nesse mês será de : R${descontos1500:.2f}')
    print(f' O Salário Líquido será de R${salario_liquido1500:.2f}')

elif salario_bruto <= 2500:
    print(f' Seu salário bruto desse mês é : R${salario_bruto:.2f}')
    print(f' Você será descontado em 5% de IR, o valor é de R$ {ir2500:.2f}')
    print(f' Você será descontado em 10% de INSS, o valor é de R$ {inss:.2f}')
    print(f' Você será descontado de 11% de FGTS, o valor é de R$ {fgts:.2f} ')
    print(f' Você será descontado em 3% do SINDICATO, o valor é de R$ {sindicato:.2f}')
    print(f' O total de descontos nesse mês será de : R${descontos2500:.2f}')
    print(f' O Salário Líquido será de R${salario_liquido2500:.2f}')

else:
    print(f' Seu salário bruto desse mês é : R${salario_bruto:.2f}')
    print(f' Você será descontado em 20% de IR, o valor é de R$ {ir:.2f}')
    print(f' Você será descontado em 10% de INSS, o valor é de R$ {inss:.2f}')
    print(f' Você será descontado de 11% de FGTS, o valor é de R$ {fgts:.2f} ')
    print(f' Você será descontado em 3% do SINDICATO, o valor é de R$ {sindicato:.2f}')
    print(f' O total de descontos nesse mês será de : R${descontos_acima:.2f}')
    print(f' O Salário Líquido será de R${salario_liquido_acima:.2f}')
