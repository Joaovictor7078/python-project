preço = float(input('\033[34mQual é o preço do produto? R$'))
novo = preço - (preço * 10 / 100)
print('\033[35mO produto que custava \033[1;33mR${:.2f}\033[35m, na promoção com desconto de 10% vai custar \033[1;33mR${:.2f}.'.format(preço, novo))
