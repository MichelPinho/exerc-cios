# FAÇA UM PROGRAMA QUE RECEBA O VALOR DE UM PRODUTO, E FORMA DE PAGAMENTO.
# DIGA AS CONDIÇÕES DE PAGAMENTO:
# À VISTA: DINHEIRO OU CHEQUE, 10% DE DESCONTO
# À VISTA NO CARTÃO, 5% DE DESCONTO
# ATÉ 2X NO CARTÃO, PREÇO NORMAL
# 3X OU MAIS NO CARTÃO, 20% DE JUROS.
print('=-=' * 30)
print('                 BEM VINDO AO MERCADO DO MICHEL            ')
print('=-=' * 30)

compras = float(input('Informe o valor das compras -> R$ '))
print('* FORMAS DE PAGAMENTO *\n Á VISTA (5% DE DESCONTO)\n CARTÃO A VISTA (ATÉ 2X) PREÇO NORMAL\n '
      'CARTÃO À PRAZO (EM ATÉ 10X) JUROS DE 20%')
print('')
f = int(input('Escolha a forma de pagamento:\n 1- À vista\n 2- Cartão à vista \n 3- Cartão em 2x \n '
              '4- Cartão à prazo (3 até 10x)  ->  '))

if f == 1:
    desconto = compras - (compras * 0.10)
    print(f'O valor das suas compras foram {compras:.2f}.Pagando à vista sairá por R$ {desconto:.2f}.')
elif f == 2:
    desconto = compras - (compras * 0.05)
    print(f'O valor das suas compras foram {compras:.2f}.Pagando no cartão sairá por R$ {desconto:.2f}.')
elif f == 3:
    prestacao = compras / 2
    print(f'O valor das suas compras foram {compras:.2f}.Pagando parcelado, sairá em 2 parcelas de R$ {prestacao:.2f}.')
else:
    compras2 = compras + (compras * 0.20)
    parcelas = int(input('Informe a quantidade de parcelas: '))
    totparcelas = compras2 / parcelas
    print(f'O valor de suas compras foram de R$ {compras:.2f}, parcelando em {parcelas}x, o valor de cada parcela é'
          f' R$ {totparcelas:.2f}.')
