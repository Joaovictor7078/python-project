valor = float(input('\033[35mQual é o valor do funcionario? R$'))
novo = valor + (valor * 15 / 100)
print('\033[34mUm funcionario que ganhava \033[1;32mR${:.2f};'.format(valor))
print('\033[34mcom 15% de almento, passa a receber \033[1;32mR${:.2f}'.format(novo))
