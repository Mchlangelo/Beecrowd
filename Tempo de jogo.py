"""
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada:
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída:
Apresente a duração do jogo conforme exemplo abaixo.

Exemplo de Entrada	:
16  2 

Exemplo de Saída:
O JOGO DUROU 10 HORA(S)
"""

a, b = input().split()
a = int(a)
b = int(b)

if a < b:
    time = b - a
else:
    time = b + 24 - a
print("O JOGO DUROU {time} HORA(S)".format(time))