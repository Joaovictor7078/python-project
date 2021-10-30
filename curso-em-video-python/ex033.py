n1 = int(input('\033[35mDigite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

#analisando quem é o menor

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#analisando quem é o maior

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('\033[33mO menor valor digitado foi \033[1;30m{}'.format(menor))
print('\033[33mO maior valor digitado foi \033[1;30m{}'.format(maior))


