print("Bem vindo ao bar caçados pela mulher")
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade < 18:
    print("O {} não pode beber, pois tem {} anos de idade".format(nome, idade))
else:
    print("O {} pode beber, pois tem {} anos de idade".format(nome, idade))