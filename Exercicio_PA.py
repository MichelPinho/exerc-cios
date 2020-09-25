# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DA PA.
termo = int(input('Informe o primeiro termo da razão de uma P.A. ->  '))
razao = int(input('Informe a razão dessa P.A. ->  '))
decimo = termo + (11 - 1) * razao
for c in range(termo, decimo, razao):
    print(c, ' ->',  end=' ')
print('FIM')

