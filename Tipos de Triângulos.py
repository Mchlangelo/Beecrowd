"""
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

"""
orden = []
A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

#ordem decrescente dos valores
orden.append(A)
orden.append(B)
orden.append(C)
orden.sort(reverse=True)

#adicionando os valores às suas respectivas variaveis
A = orden[0]
B = orden[1]
C = orden[2]


#condições para o tipo de triângulo que vai ser formado
if A >= B + C:
  print("NAO FORMA TRIANGULO")
elif A*A == B*B + C*C:
  print("TRIANGULO RETANGULO")
elif A*A > B*B + C*C:
  print("TRIANGULO OBTUSANGULO")
elif A*A < B*B + C*C:
  print("TRIANGULO ACUTANGULO")
if A == B and B == C:
  print("TRIANGULO EQUILATERO")
elif A == B or B == C:
  print("TRIANGULO ISOSCELES")
