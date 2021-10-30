dias = int(input('\033[34mQuantos dias alugados? '))
km = float(input('\033[34mQuantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('\033[35mO total a pagar é de \033[1;30mR${:.2f}'.format(pago))
