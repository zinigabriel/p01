# Nome do aluno: Gabriel Zini Ribeiro
# Matrícula: 108903
# Data: 01/06/2022
# O programa é destinado para vendas des tickets para um RU.
print('Venda de tickets')

x = int(input('Digite a matrícula (0 para visitante): '))

if x != 0:
    print()
    qtd = int(input('Número de tickets: '))
    if qtd == 0:
        print('Preço a pagar: R$0.00')
    elif qtd <=3:
        preço = qtd * 2.50
        print('Preço a pagar: R$%0.2f' %preço)
    elif qtd <= 9:
        preço = qtd * 2.20
        print('Preço a pagar: R$%0.2f' %preço)
    elif qtd >= 10:
        preço = qtd * 2.00
        print('Preço a pagar: R$%0.2f' %preço)
    else:
        print('Inválido')
else:
    print()
    print('Visitantes podem comprar apenas 1 ticket')
    print('Preço a pagar: R$15.00')
        
    
