# Nome do aluno: Gabriel Zini RIbeiro
# Matrícula: 108903
# Data: 06/07/2022
# O programa ler o número de alunos de uma turma, a nota de cada aluno.
# Depois imprime na tela a nota original e a normalizada,
# e mostra a média da turma e o número de alunos acima da média

import numpy as np

n = int(input('Qual o tamanho da turma? '))
while n <= 0:
    n = int(input('Qual o tamanho da turma? '))

maior = 0
nota = np.empty(n)
for i in range(n):
    nota[i] = float(input('Informe a nota do aluno %d (0...250): ' %(i+1)))
    while nota[i] < 0 or nota[i] > 250:
        print('Valor Incorreto')
        nota[i]= float(input('Informe a nota do aluno %d (0...250): ' %(i+1)))

    if nota[i] > maior:
        maior = nota[i]

print()
print('Aluno   Nota Original   Nota Normalizada')

fator = 100/maior
soma = 0
for j in range(n):
    print('%3d %13.1f %20.1f' %(j+1, nota[j], (nota[j]*fator)))
    soma = soma + (nota[j]*fator)

print()
media = soma/n
print('A média da turma é: %.1f' %media)

contador = 0
for i in range(n):
    if (nota[i]*fator) > media:
        contador += 1

print('Número de alunos com nota acima da média: %d' %contador)




    
        
