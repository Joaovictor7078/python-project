medida = float(input('\033[35mUma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida * 1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('\033[34mA medida de \033[33m{}m \033[34mcorresponde a:'.format(medida))
print('\033[33m{}km'.format(km))
print('\033[33m{}hm'.format(hm))
print('\033[33m{}dam'.format(dam))
print('\033[33m{}m'.format(m))
print('\033[33m{:.0f}dm'.format(dm))
print('\033[33m{:.0f}cm'.format(cm))
print('\033[33m{:.0f}mm'.format(mm))
