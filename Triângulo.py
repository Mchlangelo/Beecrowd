"""
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X
"""



A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)


if A + B > C and A + C > B and B + C > A:
  perimetro = A+B+C
  print("Perimetro =", perimetro)
else:
  area = (A+B)*C / 2
  print("Area =", area)
