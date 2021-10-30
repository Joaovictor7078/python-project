print('=-' * 12)
print('Conversor de Temperatura')
print('=-' * 12)

print('''Escolha uma das opções abaixo para fazer uma converçõa de temperatura
[ 1 ] converter de CELSIUS para KELVIN
[ 2 ] converter de KELVIN para CELSIUS
[ 3 ] converter de CELSIUS para FAHRENHEIT
[ 4 ] converter de FAHRENHEIT para CELSIUS
[ 5 ] converter de KELVIN para FAHRENHEIT
[ 6 ] converter de FAHERENHEIT para KELVIN''')
opção = int(input('Opção: '))

print('=-' * 12)

if opção == 1:
    C = float(input('Informe a temperatura em °C: '))
    K = C + 273.15
    print('A temperatura de {}°C para {:.2f}°k'.format(C, K))
elif opção == 2:
    K = float(input('Informe a temperatura em °k: '))
    C = K - 273.15
    print('A temperatura de {}°K para {:.2f}°C'.format(K, C))
elif opção == 3:
    C = float(input('Informe a temperatura em °C: '))
    F = C * 9/5 + 32
    print('A temperatura de {}°C para {:.2f}°F'.format(C, F))
elif opção == 4:
    F = float(input('Informe a temperatura em °F: '))
    C = (F - 32) * 5/9
    print('A temperatura de {}°F para {:.2f}°C'.format(F, C))
elif opção == 5:
    K = float(input('Informe a tempratura em °K: '))
    F = K - 273.15
    print('A temperatura de {}°K para {}°F'.format(K, F))
elif opção == 6:
    F = float(input('Informe a temperatura em °F: '))
    K = (F - 32) * 5/9
    print('A temperatura de {}°F para {}°K'.format(F, K))
