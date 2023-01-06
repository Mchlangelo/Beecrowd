"""
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:
https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1050.png
"""

brasilia = 61
salvador = 71
sao_paulo = 11
rj = 21
juiz_fora = 32
campinas = 19
vitoria = 27
belo_horizonte = 31

ddd = int(input())

if ddd == brasilia:
  print("Brasilia")
elif ddd == salvador:
  print("Salvador")
elif ddd == sao_paulo:
  print("Sao Paulo")
elif ddd == rj:
  print("Rio de Janeiro")
elif ddd == juiz_fora:
  print("Juiz de Fora")
elif ddd == campinas:
  print("Campinas")
elif ddd == vitoria:
  print("Vitoria")
elif ddd == belo_horizonte:
  print("Belo Horizonte")
else:
  print("DDD nao cadastrado")
