from random import shuffle
n1 = str(input('\033[33mPrimeiro aluno: '))
n2 = str(input('\033[33mSegundo aluno: '))
n3 = str(input('\033[33mTerceiro aluno: '))
n4 = str(input('\033[33mQuarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('\033[34mA ordem de apresentação será ')
print('\033[1;30m',lista)
