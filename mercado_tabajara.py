## As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contrataram para desenvolver o programa que calculará os reajustes.
## Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
## salários até R$ 280,00 (incluindo) : aumento de 20%
## salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
## salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
## salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:

## o salário antes do reajuste;
## o percentual de aumento aplicado;
## o valor do aumento;
## o novo salário, após o aumento.

sal = float(input(' Informe o seu salário: '))

aumento1 = sal * 0.2
aumento2 = sal * 0.15
aumento3 = sal * 0.1
aumento4 = sal * 0.05

faixa1 = sal + (sal * 0.2)
faixa2 = sal + (sal * 0.15)
faixa3 = sal + (sal * 0.1)
faixa4 = sal + (sal * 0.05)

if sal <= 280:
    print(f' O salário antes do reajuste era de : R${sal}')
    print(' O percentual do seu aumento foi de : 20 %')
    print(f' O valor do aumento foi de R${aumento1:.2f}')
    print(f' O novo salário após o aumento é de R${faixa1:.2f}')

elif sal < 700:
    print(f' O salário antes do reajuste era de : R${sal}')
    print(' O percentual do seu aumento foi de : 15 %')
    print(f' O valor do aumento foi de R${aumento2:.2f}')
    print(f' O novo salário após o aumento é de R${faixa2:.2f}')

elif sal < 1500:
    print(f' O salário antes do reajuste era de : R${sal}')
    print(' O percentual do seu aumento foi de : 10 %')
    print(f' O valor do aumento foi de R${aumento3:.2f}')
    print(f' O novo salário após o aumento é de R${faixa3:.2f}')

else:
    print(f' O salário antes do reajuste era de : R${sal}')
    print(' O percentual do seu aumento foi de : 5 %')
    print(f' O valor do aumento foi de R${aumento4:.2f}')
    print(f' O novo salário após o aumento é de R${faixa4:.2f}')

