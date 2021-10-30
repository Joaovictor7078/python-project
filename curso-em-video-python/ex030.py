número = int(input('\033[35mMe diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('\033[mO número {} é \033[34mPAR'.format(número))
else:
    print('\033[mO número {} é \033[34mINPAR'.format(número))
