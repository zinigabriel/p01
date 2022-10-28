# Nome do aluno: Gabriel Zini Ribeiro
# Matrícula: 108903
# Data: 22/06/2022
# O programa desenha triângulos de acordo com a largura da base inserida pelo usuário.

#entrada da largura do triângulo
valor = 0
while valor % 2 == 0:
    valor = int(input('Digite um valor ímpar para a largura do triângulo: '))
    if valor % 2 == 1:

#triângulo à esquerda   
        print()
        for i in range (valor+1):
            if i % 2 == 1:
                for j in range(i):
                    print('*',end='')
                print()

#triângulo à direita
        print()        
        for i in range (valor+1):
            if i % 2 == 1:
                for a in range(valor-i):
                    print(' ',end='')
                for j in range(i):
                    print('*',end='')
                print()

#triâgulo centralizado
        print()
        for i in range (valor+1):
             if i % 2 == 1:
                 for a in range((valor-i)//2):
                     print(' ',end='')
                 for j in range(i):
                     print('*',end='')
                 print()

#triângulo centralizado invertido
        print()
        for i in range (valor,0,-1):
             if i % 2 == 1:
                 for a in range((valor-i)//2):
                     print(' ',end='')
                 for j in range(i):
                     print('*',end='')
                 print()
        
        


