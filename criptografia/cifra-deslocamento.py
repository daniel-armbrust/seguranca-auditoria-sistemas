#
# Exemplo simples do Algoritimo da "Cifra de Deslocamento de César".
#

# Tupla para armazenar caracteres alfanuméricos.
alfanumerico = ('A', 'B', 'C', 'D', 'E', 'F', 
                'G', 'H', 'I', 'J', 'K', 'L', 
                'M', 'N', 'O', 'P', 'Q', 'R', 
                'S', 'T', 'U', 'V', 'W', 'X', 
                'Y', 'Z', 
                'a', 'b', 'c', 'd', 'e', 'f', 
                'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'w', 'x', 
                'y', 'z',
                '1', '2', '3', '4', '5', '6',
                '7', '8', '9')

# Valor do deslocamento.
deslocamento = 3

# Armazena a entrada do usuário na variável de nome mensagem.
mensagem = input('Digite sua mensagem >>> ')

# Variável para armazenar o texto que foi cifrado.
texto_cifrado = ''

i = 0
while i < len(mensagem):    
    # Retorna uma letra da mensagem do usuário.
    letra = mensagem[i]
    
    # Retorna a posição (indice) da letra no alfanumerico.
    # Caso a letra inserida pelo usuário NÃO EXISTA (ValueError),
    # será retornado a letra que encontra-se no indice 0 (letra A).
    try:
        posicao_letra_alfanumerico = alfanumerico.index(letra)
    except ValueError:
        posicao_letra_alfanumerico = 0

    # Retorna o indice da letra que foi deslocada.
    posicao_letra_deslocada = posicao_letra_alfanumerico + deslocamento

    # Retorna a letra deslocada.
    # Caso o indice informado ultrapassar os limites da tupla de
    # alfanuméricos, será retornado a letra 'A'.
    try:
        letra_deslocada = alfanumerico[posicao_letra_deslocada]
    except IndexError:
        letra_deslocada[0]
    
    # Cria o texto cifrado com as letras que foram deslocadas.
    texto_cifrado = texto_cifrado + ' ' + letra_deslocada

    i += 1

print('Texto cifrado >>>', texto_cifrado)
                               
