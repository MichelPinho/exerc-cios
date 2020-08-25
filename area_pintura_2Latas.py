#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#	Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#	comprar apenas latas de 18 litros;
#	comprar apenas galões de 3,6 litros;
#	misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
#	sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Area:"))
n = area/6*1.1
latas_18 = n/18
latas_3 = n/3.6
latas_mista_18 = n//18
aux = n % 18
latas_mista_3 = aux/3.6

if latas_18 > int(latas_18):
    latas_18 = int(latas_18)+1
total_18 = latas_18*80

if latas_3 > int(latas_3):
    latas_3 = int(latas_3)+1
total_3 = latas_3*25

if latas_mista_3 > int(latas_mista_3):
    latas_mista_3=int(latas_mista_3) + 1

total_mista= latas_mista_18*80+latas_mista_3*25
print(latas_18,"latas apenas de 18L e preço R$",total_18)
print(latas_3,"galões apenas de 3,6L e preço R$",total_3)
print(f'A melhor forma é comprar {latas_mista_18} latas de 18 L e {latas_mista_3} galões de 3,6L, totalizando R$ {total_mista}')
