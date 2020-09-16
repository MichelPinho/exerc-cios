# CALCULANDO SENO, COSSENO E TANGENTE DE UM TRIÂNGULO RETÂNGULO

import math

x = float(input('Informe o ângulo do seu triângulo:'))

cos = math.cos(math.radians(x))
se = math.sin(math.radians(x))
tg = math.tan(math.radians(x))

print(' O seno é {:.2f}\n O cosseno é {:.2f}\n A tangente é {:.2f}'.format(se, cos, tg))

