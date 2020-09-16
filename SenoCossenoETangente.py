# CALCULANDO SENO, COSSENO E TANGENTE DE UM TRIÂNGULO RETÂNGULO

import math

x = float(input('Informe o ângulo do seu triângulo:'))

cos = math.cos(x)
se = math.sin(x)
tg = math.tan(x)

print(' O seno é {:.2f}\n O cosseno é {:.2f}\n A tangente é {:.2f}'.format(se, cos, tg))

