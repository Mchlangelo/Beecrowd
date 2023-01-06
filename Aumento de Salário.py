"""
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


Salário	                  Percentual de Reajuste
0 - 400.00                          15%
400.01 - 800.00                     12%
800.01 - 1200.00                    10%
1200.01 - 2000.00                    7%
Acima de 2000.00                     4%



Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada:
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída:
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada:
400.00

Exemplo de Saída:
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

"""

salario = float(input())

if salario >= 0 and salario <= 400.00:
  novo_salario =  salario + (salario * 15) / 100
  reajuste = (salario * 15) / 100
  percentual = "15 %"
  print("Novo salario: {:.2f}".format(novo_salario))
  print("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual:", percentual)
  
elif salario >= 400.01 and salario <= 800.00:
  novo_salario =  salario + (salario * 12) / 100
  reajuste = (salario * 12) / 100
  percentual = "12 %"
  print("Novo salario: {:.2f}".format(novo_salario))
  print("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual:", percentual)

elif salario >= 800.01 and salario <= 1200.00 :
  novo_salario =  salario + (salario * 10) / 100
  reajuste = (salario * 10) / 100
  percentual = "10 %"
  print("Novo salario: {:.2f}".format(novo_salario))
  print("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual:", percentual)

elif salario >= 1200.01 and salario <= 2000.00 :
  novo_salario =  salario + (salario * 7) / 100
  reajuste = (salario * 7) / 100
  percentual = "7 %"
  print("Novo salario: {:.2f}".format(novo_salario))
  print("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual:", percentual)

elif salario > 2000.00  :
  novo_salario =  salario + (salario * 4) / 100
  reajuste = (salario * 4) / 100
  percentual = "4 %"
  print("Novo salario: {:.2f}".format(novo_salario))
  print("Reajuste ganho: {:.2f}".format(reajuste))
  print("Em percentual:", percentual)
  