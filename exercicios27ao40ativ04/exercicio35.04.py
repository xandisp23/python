'''
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.
'''
primos=[]
n = int(input("Digite um numero inteiro: "))

for x in range(1,n):
    cont=0

    for y in range(1,x+1):
        if x%y==0:
            cont+=1

    if cont<=2:
        primos.append(x)

print("Os numeros primos são:",primos)
