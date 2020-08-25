#	O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#	                      Até 5 Kg           Acima de 5 Kg
#	File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#	Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#	Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão
# Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total,
# tipo de pagamento, valor do desconto e valor a pagar.

print('                          ###   BEM VINDO AO MERCADO TABAJARA    ###')
print('\n Estamos com uma promoção incrível de carnes, confira abaixo :')
print('                          Até 5 kg                          acima de 5 kg')
print('\n Filé                     R$ 4.90                              R$ 5.80  ')
print('\n Alcatra                  R$ 5.90                              R$ 6.80')
print('\n Picanha                  R$ 6.90                              R$ 7.80')
tipo = int(input('\nInforme o tipo de carne a ser adquirida (1) Filé, (2) para Alcatra e (3) para Picanha :'))
qtd = int(input('Informe a quantidade a ser adquirida:'))
print('\nESTAMOS COM UMA PROMOÇÃO DE 5% NAS COMPRAS COM CARTÃO TABAJARA.')
pagt = int(input('\n Informe a forma de pagamento (1) dinheiro e (2) cartão Tabajara : '))

file_menor = (qtd * 4.90)
file_maior = (qtd * 5.80)
desconto_file_menor = (file_menor - (file_menor * 0.05))
desconto_file_maior = (file_maior - (file_maior * 0.05))
alcatra_menor = (qtd * 5.90)
alcatra_maior = (qtd * 6.80)
desconto_alcatra_menor = (alcatra_menor - (alcatra_menor * 0.05))
desconto_alcatra_maior = (alcatra_maior - (alcatra_maior * 0.05))
picanha_menor = (qtd * 6.90)
picanha_maior = (qtd * 7.80)
desconto_picanha_menor = (picanha_menor - (picanha_menor * 0.05))
desconto_picanha_maior = (picanha_maior - (picanha_maior * 0.05))

## teste do filé até 5 kg e após 5 kg:
if tipo == 1:
    if qtd <= 5:
        if pagt == 1:
            print(f'O valor a ser pago será de :{file_menor:.2f}')
        else:
            print(f' O valor a ser pago com desconto é de R${desconto_file_menor:.2f}')

    else:
        if pagt == 1:
            print(f'O valor a ser pago será de :{file_maior:.2f}')
        else:
            print(f' O valor a ser pago com desconto é de R${desconto_file_maior:.2f}')

## teste da alcatra de até 5kg e após 5kg:
if tipo == 2:
    if qtd <= 5:
        if pagt == 1:
            print(f'O valor a ser pago será de :{alcatra_menor:.2f}')
        else:
            print(f' O valor a ser pago com desconto é de R${desconto_alcatra_menor:.2f}')

    else:
        if pagt == 1:
            print(f'O valor a ser pago será de :{alcatra_maior:.2f}')
        else:
            print(f' O valor a ser pago com desconto é de R${desconto_alcatra_maior:.2f}')

## teste de picanha de até 5 kg e após 5 kg:
if tipo == 3:
    if qtd <= 5:
        if pagt == 1:
            print(f'O valor a ser pago será de :{picanha_menor:.2f}')
        else:
            print(f' O valor a ser pago com desconto é de R${desconto_picanha_menor:.2f}')

    else:
        if pagt == 1:
            print(f'O valor a ser pago será de :{picanha_maior:.2f}')
        else:
            print(f' O valor a ser pago com desconto é de R${desconto_picanha_maior:.2f}')
