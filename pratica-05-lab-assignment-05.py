# Nome do aluno: Gabriel Zini Ribeiro
# Matrícula: 108903
# Data: 07/06/2022
# (breve comentário dizendo o que o programa faz)

import turtle as Tut
import fechadura

# Altere o comando simples de leitura abaixo para que o programa só continue
# se for digitado um valor dentro do intervalo correto.
# Obs.: Não é necessário escrever nenhuma mensagem de erro se a pessoa digitar
#       um valor inválido. Basta ler o valor novamente.

a = False
while a == False:
    matricula = int( input("Digite o número de sua matrícula (1 a 9999999): "))
    if matricula >= 1 and matricula <= 9999999:
        a = True
    else:
        a = False	

# A linha seguir desenha a fechadura na tela. Favor não alterá-la
fechadura.contorno( Tut, matricula )

# Escreva o restante de seu código abaixo desta linha

a = False
while a == False:
    Tut.fd(40)
    d = matricula % 10
    matricula = matricula // 10 
    if d != 0:
        if d % 2 == 0: #o número é ímpar
            Tut.right(90)
            Tut.fd(d*10)
            Tut.bk(d*10)
            Tut.left(90)
        if d % 2 != 0:
            Tut.left(90)
            Tut.fd(d*10)
            Tut.bk(d*10)
            Tut.right(90)
    if matricula == 0:
        a = True
    else:
        a = False

# A linha a seguir deve ser a última do programa. Favor não alterá-la
Tut.Screen().exitonclick()
