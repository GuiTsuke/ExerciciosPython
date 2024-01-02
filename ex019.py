from random import choice
print('Sorteio')
aluno1 = str(input('1º Aluno: '))
aluno2 = str(input('2º Aluno: '))
aluno3 = str(input('3º Aluno: '))
aluno4 = str(input('4º ALuno: '))
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
print('Aluno sorteado: {}'.format(choice(lista_alunos)))