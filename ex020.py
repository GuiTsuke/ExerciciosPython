from random import shuffle
al1 = str(input('1º Aluno: '))
al2 = str(input('2º Aluno: '))
al3 = str(input('3º Aluno: '))
al4 = str(input('4º Aluno: '))

list1 = [al1, al2, al3, al4]
shuffle(list1)
print('Sorteio da Ordem de Apresentação')
print('1ªApresentação: {}'.format(list1[0]))
print('2ªApresentação: {}'.format(list1[1]))
print('3ªApresentação: {}'.format(list1[2]))
print('4ªApresentação: {}'.format(list1[3]))
