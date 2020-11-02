# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO, DEPOIS APRESENTE UM QUANTIDADE X DOS PRIMEIROS ELEMENTOS DE
# UMA SEQUÊNCIA DE FIBONACCI
# FÓRMULA : Fn = Fn - 1 + Fn - 2
# EX: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

n = int(input('Informe quantos termos da sequencia de Fibonacci você quer mostrar -> '))

t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')

cont = 3
while cont <= n:
   t3 = t1 + t2
   print('- {}'.format(t3), end='')
   t1 = t2
   t2 = t3
   cont += 1
print('- FIM')
