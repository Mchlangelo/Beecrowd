"""
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

"""

num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

lista = []

lista.append(num1)
lista.append(num2)
lista.append(num3)

lista.sort() 

for valores in lista:
  print(valores)
  
print()

print(num1)
print(num2)
print(num3)
