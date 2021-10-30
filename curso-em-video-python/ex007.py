n = float(input('\033[36mPrimeira nota do aluno: '))
s = float(input('\033[36mSegunda nota do aluno: '))
média = (n + s) / 2
print('\033[33mA média entre \033[m{:.1f} \033[33me \033[m{:.1f} \033[33mé igual a \033[m{:.1f}'.format(n, s, média))
