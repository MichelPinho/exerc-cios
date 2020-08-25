#	Faça um programa que leia e valide as seguintes informações:
#	Nome: maior que 3 caracteres;
#	Idade: entre 0 e 150;
#	Salário: maior que zero;
#	Sexo: 'f' ou 'm';
#	Estado Civil: 's', 'c', 'v', 'd';


nome = str(input('Digite seu nome:'))

while len(nome) < 3:
    print('nome inválido')
    str(input('Digite seu nome:'))
else:
    print('Nome validado')

idade = int(input('Digite a sua idade :'))

while idade < 0 or idade > 150:
    print('Idade inválida')
    input('Digite a sua idade :')
else:
    print('Idade validada')

salario = float(input('Informe seu salário : '))

while salario < 0:
    print('ERRO: salário menor que 0, refaça a operação')
    (float('Informe seu salário : '))
else:
    print('Salário válido')

sexo = input('Informe seu sexo (M) ou (F): ').lower()

while sexo != 'm' and 'f':
    print(' ERRO: sexo inválido, repita a operação')
    input('Informe seu sexo (M) ou (F): ').lower()
else:
    print('Sexo validado')

estado = input('Informe seu estado civil casado (C), solteiro(S), viúvo (V) ou disquitado (D):').lower()

while estado != 'c' and estado != 's' and estado != 'v' and estado != 'd':
    print('ERRO: Estado civil inválido, repita a operação')
    input('Informe seu estado civil casado (C), solteiro(S), viúvo (V) ou disquitado (D):')

else:
    print('Estado civil validado')
    print('\nObrigado')

