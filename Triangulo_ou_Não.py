# FAÇA UM PROGRAMA QUE RECEBA A MEDIDA DE 3 RETAS, E DIGA SE PODE FORMAR UM TRIÂNGULO OU NÃO.
# REGRA BÁSICA , O LADO MAIOR NÃO PODE SER MAIOR QUE A SOMA DOS OUTROS 2 LADOS.

l1 = float(input('Informe o lado do triângulo:'))
l2 = float(input('Informe o lado do triângulo:'))
l3 = float(input('Informe o lado do triângulo:'))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Sim, com essas medidas pode-se formar um triângulo.')
else:
    print('Não, com essas medidas não pode ser formado um triângulo.')

