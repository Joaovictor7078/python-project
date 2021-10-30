from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('\033[35m-=-' * 20)
print('\033[mVou pensar em um número entre 0 e 5. Tente advinhar...')
print('\033[35m-=-' * 20)
jogador = int(input('\033[mEm que número eu pensei? ')) # jogador tenta advinhar
print('\033[33mPROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[mPARABÉMS! Você conseguiu me vencer!')
else:
    print('\033[mGANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
















