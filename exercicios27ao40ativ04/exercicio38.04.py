'''
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
1.	Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
2.	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
3.	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário.
 Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
'''

salario = float(input("Dgite o salário inicial do funcionário em 1995: "))
ano = 1995
ano_atual = int(input("Digite em que ano estamos: "))
aumento = 1.5 / 100

while ano < ano_atual:
    ano += 1
    salario *= 1 + aumento
    aumento *= 2

print(f"O salario em {ano} é de R$ {salario:.2f}")