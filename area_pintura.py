#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

num1 = int(input(' Qual a área em M2 que deverá ser pintada ? : '))

cobertura_litros = float(num1 / 3)

lata = int(round(cobertura_litros/18))

gasto = int(lata * 80)

print(f'A quantidade de latas a serem usadas serão {lata} , e o valor a ser pago será de R${gasto:.2f} ')
