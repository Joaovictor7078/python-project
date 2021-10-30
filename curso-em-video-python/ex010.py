real = float(input('\033[34mQuanto de dinheiro você tem na sua carteira: R$'))
dolar = real / 3.70
print('\033[mCom \033[35mR${:.2f} \033[mvocê pode comprar \033[35mUS${:.2f}'.format(real, dolar))
