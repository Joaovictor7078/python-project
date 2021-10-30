print('\033[1;32m-=' * 20)
print('\033[1;33maAnalisador de Triângulos')
print('\033[1;32m-=' * 20)

r1 = float(input('\033[35mPrimeiro segmento: '))
r2 = float(input('\033[35mSegundo segmento: '))
r3 = float(input('\033[35mTerceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0mOs segmentos a cima \033[1;34mPODEM FORMAR triângulo')

else:
    print('\033[0mOs segmentos a cima \033[1;34mNÃO PODEM FORMAR triângulos')

   # print('Os segmentos a cima PODEM FORMAr
#triângulo')