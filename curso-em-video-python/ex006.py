n = int(input('\033[35mDigite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('\033[34mO dobro de \033[m{} \033[34mvale \033[m{}'.format(n, d))
print('\033[34mO triplo de \033[m{} \033[34mvale \033[m{}'.format(n, t))
print('\033[34mA raiz quadrada de \033[m{} \033[34mé igual a \033[m{:.2f}.'.format(n, r))


