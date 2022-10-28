#Nome: Gabriel Zini RIbeiro
#Matrícula: 108903
#Data: 29/06/2022
#O programa abaixo cria um arranjo com as dimenções dada pelo usário e calcula a média dos valores presentes no índice,
#além de imprimir a quantidade de númueros que são menores que a media.

import numpy as np
tam = 10
# ler o tamanho do arranjo
N = int(input('Informe o tamanho do arranjo (>=%d): ' %tam))
while N < tam :
    N = int(input('Informe o tamanho do arranjo (>=%d): '  %tam))
# definir o limite inferior
inf = int(input('Informe o limite inferior (>=0): '))
while inf < 0 :
    inf = int(input('Informe o limite inferior (>=0): '))
    
################################################################################
#### substitua o comando abaixo pelo código para implementar o item "a" do roteiro #
#definir o limite superior
    
sup = int(input('Informe o limite superior (>%d): ' %inf))
while sup <= inf :
    print('O limite superior deve ser maior que o limte inferior')
    sup = int(input('Informe o limite superior (>%d): ' %inf))
    
# iniciar gerador de números aleatórios com 0
# para gerar os mesmos números dos exemplos do roteiro
np.random.seed( 0 )
# gerar um arranjo de dimensao N com valores inteiros aleatórios no intervalo
# [inf, sup]
num = np.random.randint(inf, sup+1, N)
# mostra os valores se o arranjo for pequeno (até 20)
if N > 20:
    print('\nValores não serão exibidos - Arranjo muito grande.')
else:
    print('\nValores Gerados: ', end="")
    print(num)
#####################################################################################
# inclua abaixo desta linha o código para implementar os itens "b" e "c" do roteiro #
quociente = 0
soma = 0
for i in range (0, len(num)):
    if num[i] % 2 != 0:
        soma = soma + num[i]
        quociente += 1
media = soma/quociente
media = round(media)
print('A média inteira dos ímpares é: %d' %media)

contador = 0
for i in range(0, len(num)):
    if num[i] < media:
        contador += 1
print('O número de valores menores do que %d é: %d' %(media,contador))
        

    


