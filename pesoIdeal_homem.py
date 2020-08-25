#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

num1 = float(input(' Digite aqui a sua altura em metros "M" : '))


conv = float((72.7*num1) - 58)

print(' O seu peso ideal é : %s' % conv)
