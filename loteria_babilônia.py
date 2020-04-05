num_correto = 7
chances = 3

while chances > 0:
    print('Você tem {} chances para tentar acertar o número'.format(chances))
    num_aposta = int(input('Teste sua sorte digitando um número: '))
    if num_aposta == num_correto:
        print('Você acertou, procure a lotérica mais próxima para sacar o dinheiro')
        break
    elif num_aposta < num_correto:
        print('Tente um número maior')    
    else:
        print('Tente um número menor')
    chances -= 1
if chances == 0:
    print('Suas chances de acertar se esgotaram, tente novamente outro dia')