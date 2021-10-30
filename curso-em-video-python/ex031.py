distância = float(input('\033[33mQual é a distancia da sua viagem? '))
print('\033[35mVocê está preste a começar uma viagem de \033[1;30m{}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('\033[35mE o preço de sua passagem será de \033[1;30mR${:.2f}'.format(preço))

#outro metodo!!!


