# ESCREVA UM PROGRAMA QUE RECEBA O SALÁRIO DE UM FUNCIONÁRIO
# SE ELE RECEBER ATÉ R$ 1.200,00 , TERÁ UM AUMENTO DE 10 %
# SE ELE RECEBER MENOS, TERÁ UM AUMENTO DE 15 %.

s = float(input('Informe seu salário (sem pontos ou vírgulas): '))
a10 = s * 1.10
a15 = s * 1.15
if s <= 1200:
    print(f'O seu novo salário com reajuste será de R$ {a10:.2f}')
else:
    print(f'O seu novo salário com reajuste será de R$ {a15:.2f}')
