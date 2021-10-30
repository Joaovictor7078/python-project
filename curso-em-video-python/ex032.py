from datetime import date
ano = int(input('\033[35mQue ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=rmat(ano)0 or ano % 400 == 0:
    print('\033[33mO ano \033[1;30m{} \033[33mé BISSEXTO'.format(ano))
else:
    print('\033[33mO ano \033[1;30m{} \033[33mNÃO é BISSEXTO'.fo