# Nome do aluno: Gabriel Zini Ribeiro   
# Matrícula: 108903
# Data: 11/05/2022
# Esse sistema cria um labirinto de acordo com o número presente na variável matricula,
# logo após o programa faz a tartaruga Tut percorrer o caminho no labirinto até o tomate.

import turtle as Tut
import p01_maze as m

############# Troque, na linha de baixo, o 0 pelo número de sua matrícula ### 
matricula = 108903



m.build_maze( Tut, matricula ) 

############################################
##  Adicione seu código abaixo desta linha
############################################


Tut.fd(100)
Tut.right(90)
Tut.fd(100)
Tut.left(90)
Tut.fd(150)
Tut.right(90)
Tut.fd(100)
Tut.left(90)
Tut.fd(100)
Tut.right(90)
Tut.fd(100)
Tut.right(90)
Tut.fd(100)
Tut.left(90)
Tut.fd(150)
Tut.left(90)
Tut.fd(200)


############################################
## Seu código não deve passar desta linha
############################################
Tut.Screen().exitonclick()
