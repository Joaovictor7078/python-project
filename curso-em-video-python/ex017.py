from math import hypot
co = float(input('\033[32mComprimento do cateto oposto: '))
ca = float(input('\033[32mComprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\033[34mA hipotenusa vai medir \033[1;30m{:.2f}'.format(hi))
