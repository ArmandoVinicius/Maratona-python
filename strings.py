print('Olá, seja bem vindo!') # Exibe uma mensagem na tela
nome = input('Digite seu nome: ') # Exibe uma mensagem e espera o usuário digitar
print( 'Olá ', nome, ', seja bem vindo!', sep="" ) # Exibe uma mensagem com o nome do usuário
# O sep="" define que não haverá separação entre as strings concatenadas

type( nome ) # Retorna o tipo da variável

nome_maiusculo = nome.upper() # Retorna em maiusculo
nome_minusculo = nome.lower() # Retorna em minusculo
nome.lower().replace( "a", "b" ) # Substitui o 1º parâmetro pelo 2º parâmetro 
qtd_char = len( nome ) # Retorna a quantidade de caracteres de nome

nome = "Armando Vinicius"
nome[ -1 ] # Retorna o caractere correspondente ao indice na palavra ( começa do zero )

nome[8:12] # Fatiamento { Slice }, nome[start:stop]
nome[:3] # Se o start for zero, não é necessário especificar o start
nome[:] # Se o stop for o final da string, não é necessário especificar
nome[::] # nome[start:stop:step] <- sintaxe completa
nome[::-1] # Se o step for -1, ele começa do final

nome.find( " " ) # Retorna o indice do parâmetro indicado