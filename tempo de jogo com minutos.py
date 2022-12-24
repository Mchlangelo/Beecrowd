"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

saida:
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)”
"""

a, c, b, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

dif= ((b*60)+d)-((a*60)+c)
if dif <= 0:
    dif += 24 * 60
    
time = dif // 60
minute = dif % 60
print("O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)".format(time,minute))
