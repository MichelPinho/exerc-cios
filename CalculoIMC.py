print (" Bem vindo a calculadora IMC ")

nome = input("digite seu nome:")

altura = float(input("digite sua altura :"))

peso = float(input("digite seu peso :"))

imc = peso / (altura * altura)

print(f'{nome}, seu IMC é : {imc:.2f}')

if imc <= 18.4:

    print("ABAIXO DO PESO")

elif imc > 18.5 and imc <= 24.9:

    print("PESO NORMAL")

elif imc >25 and imc <= 29.9:

    print("SOBREPESO")

elif imc >30 and imc <= 34.9:

    print("OBESIDADE GRAU I")

elif imc >35 and imc <=39.9:

    print("OBESIDADE GRAU II")

elif imc >40:

    print("OBESIDADE GRAU III MÓRBIDA")




























