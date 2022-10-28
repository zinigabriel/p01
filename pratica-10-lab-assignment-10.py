# Nome do aluno: Gabriel Zini Ribeiro
# Matrícula:108903
# Data: 13/07/2022
# O programa imprime uma matriz de tamanho n.
# Compara os vizinhos das células que não são das extremidades da matriz.
# Caso uma célula possua um valor maior que o valor presente nas células vizinhas
# essa célula será imprimida na imprensão 'picos encontrados'.

import numpy as np

#criando a matriz de tamnanho n
np.random.seed(1)
n = int(input('tamanho: '))
m = np.random.randint(0,11,(n,n))
        
print()

#imprimindo a matriz
print('Território completo')
for i in range(len(m)):
    for j in range(len(m)):
        print('%3d'%m[i][j], end='' )
    print()

print()

#imprimindo apenas o maior termo da matriz
print('Pico encontrados')
for i in range(len(m)):
    for j in range(len(m)):
        if i != 0 and j!= 0 and i != n-1 and j != n-1:
            if m[i][j] >= m[i-1][j] and m[i][j] >= m[i][j-1] and m[i][j] >= m[i+1][j] and m[i][j] >= m[i][j+1]:
                print('%3d' %m[i][j], end='')
            else:
                print('   ', end='')
        else:
                print('   ', end='')
    print()
    



