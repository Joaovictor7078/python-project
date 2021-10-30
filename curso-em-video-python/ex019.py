from random import choice
n1 = str(input('\033[34mPrimeiro aluno: '))
n2 = str(input('\033[34mSegundo aluno: '))
n3 = str(input('\033[34mTerceiro aluno: '))
n4 = str(input('\033[34mQuarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('\033[35mO aluno escolhido foi: \033[1;30m{}'.format(escolhido))
