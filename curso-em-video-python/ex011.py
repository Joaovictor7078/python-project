largura = float(input('\033[36mLargura da parede: '))
altura = float(input('\033[36mAltura da parede: '))
aréa = largura * altura
print('\033[30mSua parede tem a dimensão de \033[34m{}x{} \033[30me sua aréa e de \033[34m{}m²'.format(largura, altura, aréa))
tinta = aréa / 2
print('\033[30mPara pintar esta parede, você precisará de \033[34m{}L \033[30mde tinta.'.format(tinta))
