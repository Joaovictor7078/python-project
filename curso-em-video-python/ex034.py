salário = float(input('Qual é o salério do funcionario R$'))
if salário <= 1250:
    NOVO = salário + (salário * 15 / 100)
else:
    NOVO = salário + (salário * 10 / 100)
print('Quem recebia \033[31mR${:.2f} \033[0mpassa a receber \033[32mR${:.2f} \033[0magora.'.format(salário, NOVO))
