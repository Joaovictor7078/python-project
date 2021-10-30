nome = str(input('\033[35mQual é seu nome completo? ')).strip()
print('\033[33mSeu nome tem Silva? \033[1;30m{}'.format('silva' in nome.lower()))
