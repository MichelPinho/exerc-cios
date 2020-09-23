# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA PEDIRÁ O VALOR DA CASA
# E O SALÁRIO DO COMPRADOR, E EM QUANTOS ANOS ELE VAI PAGAR.
# CALCULE O VALOR DA PRESTAÇÃO MENSAL, SABENDO QUE A PRESTAÇÃO NÃO PODE PASSAR DE 30% DO SALÁRIO, SE NÃO, O EMPRÉSTIMO
# SERÁ NEGADO.
casa = float(input('Informe o valor da casa -> '))
salario = float(input('Informe o seu salário -> '))
prestacao = int(input('Em quantas prestações (meses) você gostaria de pagar seu financiamento ? '))

mensal = casa / prestacao
aprovado = salario * 0.30

if mensal <= aprovado:
    print(f'O seu financiamento foi aprovado, e você pagará R$ {mensal:.2f} em {prestacao} prestações.')
else :
    print(f'Seu financiamento não foi aprovado.')
    print(f'prestação de R${mensal:.2f},excedeu a sua margem R$ {aprovado:.2f} que é (30% do salário).')


