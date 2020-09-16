# CALCULANDO A HIPOTENUSA DE UM TRIÂNGULO
import math

x = float(input('Informe o cateto oposto:'))
y = float(input('Informe o cateto adjacente:'))
hi = math.hypot(x, y)

print('A hipotenusa do seu triângulo retângulo é:{:.2f}'.format(hi))

