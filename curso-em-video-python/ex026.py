frase = str(input('\033[32mDigite uma frase: ')).upper().strip()
print('\033[35mA letra A aparece \033[1;30m{} \033[35mvezes na frase. '.format(frase.count('A')))
print('\033[35mA primeira letra A apareceu na posição \033[1;30m{}'.format(frase.count('A')+1))







