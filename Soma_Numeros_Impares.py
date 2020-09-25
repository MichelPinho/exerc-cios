# FAÇA UM PROGRAMA QUE CALCULE A SOMA DE TODOS OS NÚMEROS ÍMPARES , QUE SÃO MÚLTIPLOS DE 3 ,
# NO INTERVALO DE 1 ATE 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'Pronto, já somei tudo. São {cont} números somados, totalizando {soma} números ímpares.')
