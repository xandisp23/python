'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
'''

cd = int(input("Qual a quantidade de cds ? "))
valor = float(input("Qual preço de cada cd ? "))

Total_inv = (cd*valor)
Media_cd = (Total_inv / cd)

print("O valor total investido nos cd`s foi de: R$", Total_inv)
print("A média de preço pago por cada cd foi de: R$", Media_cd)