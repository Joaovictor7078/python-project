nome = str(input('Qual é o seu nome? '))
idade = int(input('Quantos anos você tem? '))
altura = float(input('Qual é a sua altura? '))
if 18 >= idade:
    print('Foi um prazer te conhecer {}\nVocê é tão jovem.'.format(nome, idade))
else:
    print('Foi um prazer te conhecer {}.'.format(nome))
