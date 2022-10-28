# Nome do aluno:Gabriel Zini Ribeiro
# Matrícula:108903
# Data:18/05/2022
# (breve comentário dizendo o que o programa faz)

nome = 'Universidade Federal de Viçosa'
alunos = 10620         # alunos de graduação matriculados no campus Viçosa
rel_cand_vagas = 11.3  # relação candidatos / vagas total
area = 2353.94         # área física total em hectares (ha)

print()             # este comando imprime uma linha em branco
print('Nome da instituição:                          ',nome)
print('Alunos de grad. matriculados no campus Viçosa:', alunos)
print('Relação candidatos / vagas total:             ', rel_cand_vagas)
print(f'Área total do campus Viçosa:                   {area} ha')
print()
print('Área total do campus Viçosa (ha):')
print('Usando largura 7 e 2 casas decimais: %7.2f' %area)
print('Usando largura 9 e 2 casas decimais: %9.2f' %area)
print('Usando largura 9 e 3 casas decimais: %9.3f' %area)
print('Usando largura 9 e nenhuma casa decimal: %9.0f' %area)
print()
curso = str(input('Qual o seu curso? '))
ingresso = int(input('Em que ano voçê iniciou seu curso? '))
periodo = (2022 - ingresso)*2 + 1
print(f'Você está no {periodo}º perido de {curso}.')
