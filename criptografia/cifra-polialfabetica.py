#
# Exemplo simples do Algoritimo da "Cifra Polialfabética".
#

# Dicionário que contém o mapeamento de um carácter para
# um conjunto de caracteres.
alfanumerico = {'A': 'yBc', 'B': 'aef', 'C': '9jT', 
                'D': 'OOi', 'E': '45j', 'F': 'yOy', 
                'G': '7g5', 'H': '6NN', 'I': 'oLE', 
                'J': 'Bm8', 'K': 'PPv', 'L': 'bVv', 
                'M': 'XR7', 'N': 'UUS', 'O': '2B5', 
                'P': 'p8k', 'Q': 'ErT', 'R': 'bRz', 
                'S': 'G6H', 'T': 'v67', 'U': 'cXX', 
                'V': 'pF7', 'W': 'cTY', 'X': '66M', 
                'Y': '7w3', 'Z': 'wW9', 
                'a': 'nG3', 'b': 'x56', 'c': 'BbZ', 
                'd': 'oF7', 'e': 'O0O', 'f': '5tG', 
                'g': 'b7U', 'h': 'uWd', 'i': '636', 
                'j': 'oh5', 'k': 'xGx', 'l': 'jL6', 
                'm': '8hB', 'n': 'SSd', 'o': 'bSk', 
                'p': 'JnY', 'q': 'pU1', 'r': '1yD', 
                's': '9vV', 't': 'ai6', 'u': 'fRr', 
                'v': 'RWe', 'w': 'LxL', 'x': '4HK', 
                'y': 'h6S', 'z': 'S7s', 
                '1': '0oC', '2': 'xRz', '3': 'gWq', 
                '4': 'qZX', '5': '111', '6': 'v55',
                '7': 'a33', '8': 'YVX', '9': '45F'}

# Armazena a entrada do usuário na variável de nome mensagem.
mensagem = input('Digite sua mensagem >>> ')

# Variável para armazenar o texto que foi cifrado.
texto_cifrado = ''

i = 0
while i < len(mensagem):    
    # Retorna uma letra da mensagem do usuário.
    letra = mensagem[i]

    # Retorna o conjuto de caracteres que representa a letra.
    # Caso a letra inserida pelo usuário NÃO EXISTA (ValueError),
    # será retornado o conjunto de caracteres que representa a 
    # letra A.    
    try:
        conjunto_caracteres = alfanumerico[letra]        
    except KeyError:
        conjunto_caracteres = alfanumerico['A']
    
    # Cria o texto cifrado com as letras que foram deslocadas.
    texto_cifrado = texto_cifrado + ' ' + conjunto_caracteres
    
    i += 1

print('Texto cifrado >>>', texto_cifrado)