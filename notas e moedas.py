N = float(input())

cem, R1 = divmod(N, 100)
cinquenta, R2 = divmod(R1, 50)
vinte, R3 = divmod(R2, 20)
dez, R4 = divmod(R3, 10)
cinco, R5 = divmod(R4, 5)
dois, R6 = divmod(R5, 2)
um, R7 = divmod(R6, 1)
cinquentaC, R8 = divmod(R7, 0.5)
vintecincoC, R9 = divmod(R8, 0.25)
dezC, R10 = divmod(R9, 0.1)
cincoC, R11 = divmod(R10, 0.05)
umC = round((R11+0.009) // 0.01)

print("NOTAS:")
print("%i nota(s) de R$ 100.00" % cem)
print("%i nota(s) de R$ 50.00" % cinquenta)
print("%i nota(s) de R$ 20.00" % vinte)
print("%i nota(s) de R$ 10.00" % dez)
print("%i nota(s) de R$ 5.00" % cinco)
print("%i nota(s) de R$ 2.00" % dois)
print("MOEDAS:")
print("%i moeda(s) de R$ 1.00" % um)
print("%i moeda(s) de R$ 0.50" % cinquentaC)
print("%i moeda(s) de R$ 0.25" % vintecincoC)
print("%i moeda(s) de R$ 0.10" % dezC)
print("%i moeda(s) de R$ 0.05" % cincoC)
print("%i moeda(s) de R$ 0.01" % umC)


"""
#OUTRA SOLUÇÃO

N = float(input(" "))
print("{} nota(s) de R$ 100.00".format(int(N//100)))
N %= 100
print("{} nota(s) de R$ 50.00".format(int(N//50)))
N %= 50
print("{} nota(s) de R$ 20.00".format(int(N//20)))
N %= 20
print("{} nota(s) de R$ 10.00".format(int(N//10)))
N %= 10
print("{} nota(s) de R$ 5.00".format(int(N//5)))
N %= 5
print("{} nota(s) de R$ 2.00".format(int(N//2)))
N %= 2


print("MOEDAS:")

print("{} moeda(s) de R$ 1.00".format(int(N//1.00)))
N %= 1.00
print("{} moeda(s) de R$ 0.50".format(int(N//0.50)))
N %= 0.50
print("{} nota(s) de R$ 0.25".format(int(N//0.25)))
N %= 0.25
print("{} moeda(s) de R$ 0.10".format(int(N//0.10)))
N %= 0.10
print("{} moeda(s) de R$ 0.05".format(int(N//0.05)))
N %= 0.05
print("{} moeda(s) de R$ 0.01".format(int(N//0.01)))
N %= 0.01
"""
