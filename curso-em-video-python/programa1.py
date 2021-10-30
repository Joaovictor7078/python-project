nome = str(input('Qual é o seu nome? '))
idade = int(input('Quantos anos você tem? '))
print('Olá {} é um prazer te conhecer'.format(nome))

#Estrutura da idade
if idade >= 10 and idade < 20:
    print('{}, Você tem {} anos de idade, e esta jovem.'.format(nome, idade))
elif idade >= 20 and idade < 50:
    print('{}, Você tem {} anos de idade, e é adulto(a).'.format(nome, idade))
elif idade >= 50:
    print('{}, Você tem {} anos de idade, e é idoso(a).'.format(nome, idade))
print('Hello World')
