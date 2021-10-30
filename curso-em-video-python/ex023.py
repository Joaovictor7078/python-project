num = int(input('\033[33mInforme um valor: '))
u = num //1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('\033[34mAnalisando o número \033[1;35m{}'.format(num))
print('\033[34mUnidade: \033[1;35m{}'.format(u))
print('\033[34mDezena: \033[1;35m{}'.format(d))
print('\033[34mCentena: \033[1;35m{}'.format(c))
print('\033[34mMilhar: \033[1;35m{}'.format(m))
