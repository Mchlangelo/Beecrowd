"""
Com base na tabela abaixo, escreva um programa que leia o código de um item e a 
quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

A tabela:
cachorro_quente = R$ 4.00
x_salada = R$ 4.50
x_bacon = R$ 5.00
torrada_simples = R$ 2.00
refrigerante = R$ 1.50

Entrada:
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída:
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, 
com 2 casas após o ponto decimal.

"""

codigo, qtd = input("").split()
codigo = int(codigo)
qtd = int(qtd)

cachorro_quente = 4.00
x_salada = 4.50
x_bacon = 5.00
torrada_simples = 2.00
refrigerante = 1.50

if codigo == 1:
  preco_cachorro = cachorro_quente * qtd
  print("Total: R$ {:.2f}".format(preco_cachorro))

if codigo == 2:
  preco_salada = x_salada * qtd
  print("Total: R$ {:.2f}".format(preco_salada))

if codigo == 3:
  preco_bacon = x_bacon * qtd
  print("Total: R$ {:.2f}".format(preco_bacon))

if codigo == 4:
  preco_torrada = torrada_simples * qtd
  print("Total: R$ {:.2f}".format(preco_torrada))

if codigo == 5:
  preco_refrigerante = refrigerante * qtd
  print("Total: R$ {:.2f}".format(preco_refrigerante))