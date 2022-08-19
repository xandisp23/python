'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
'''
import math
alunos = int(input("Quantidade de Alunos: "))
turmas = int(input("Quantidade de turmas: "))

media = math.ceil(alunos / turmas)
if media >= 41:
    print("Não é possivel preencher as turmas")
else:
    print(media,"alunos(a) por turma")