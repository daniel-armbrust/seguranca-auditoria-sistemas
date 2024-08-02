#
# Simples script em Python usado para verificar strings e HASHs.
#

# Bibliotecas usadas.
import os
import time
import hashlib

#
# Constantes.
#
VERMELHO = '\033[31m'
VERDE = '\033[32m'
RESET = '\033[0m'

#
# Funções.
#
def limpa_tela():    
    if os.name == 'nt':
        # Limpa tela Windows.
        os.system('cls')
    else:
        # Limpa tela Linux, MacOS.
        os.system('clear')
    

def verifica_hash_md5():
    #
    # Função usada para verificar o HASH MD5
    #
    print('\nVerifica VALOR HASH MD5')
    print('-----------------------\n')

    # Obtém o texto do usuário.
    texto = input('Digite uma linha de texto >>> ')

    # Obtém o hash do usuário.
    hash_md5_entrada = input('Digite o valor HASH para ser verificado >>> ')

    # A string é convertida em bytes, pois a função hash espera uma 
    # entrada em formato de bytes.
    texto_bytes = texto.encode()

    # A função md5() é chamada para criar um objeto hash.
    objeto_hash = hashlib.md5(texto_bytes)

    # O método hexdigest() é usado para obter a representação 
    # hexadecimal do hash.
    hash_md5_saida = objeto_hash.hexdigest()

    if hash_md5_entrada == hash_md5_saida:
        print(VERDE + '!!! VALOR HASH MD5 VALIDADO COM SUCESSO !!!')
    else:
        print(VERMELHO + '!!! ERRO AO VALIDAR VALOR HASH MD5 !!!')
    

def verifica_hash_sha1():
    #
    # Função usada para verificar o HASH SHA-1
    #
   
    print('\nVerifica VALOR HASH SHA-1')
    print('-------------------------\n')

    # Obtém o texto do usuário.
    texto = input('Digite uma linha de texto >>> ')

    # Obtém o hash do usuário.
    hash_md5_entrada = input('Digite o valor HASH SHA-1 para ser verificado >>> ')

    # A string é convertida em bytes, pois a função hash espera uma 
    # entrada em formato de bytes.
    texto_bytes = texto.encode()

    # A função sha1() é chamada para criar um objeto hash.
    objeto_hash = hashlib.sha1(texto_bytes)

    # O método hexdigest() é usado para obter a representação 
    # hexadecimal do hash.
    hash_md5_saida = objeto_hash.hexdigest()

    if hash_md5_entrada == hash_md5_saida:
        print(VERDE + '!!! VALOR HASH SHA-1 VALIDADO COM SUCESSO !!!')
    else:
        print(VERMELHO + '!!! ERRO AO VALIDAR VALOR HASH SHA-1 !!!')


def verifica_hash_sha256():
    #
    # Função usada para verificar o HASH SHA-256
    #

    print('\nVerifica VALOR HASH SHA-256')
    print('---------------------------\n')

    # Obtém o texto do usuário.
    texto = input('Digite uma linha de texto >>> ')

    # Obtém o hash do usuário.
    hash_md5_entrada = input('Digite o valor HASH SHA-256 para ser verificado >>> ')

    # A string é convertida em bytes, pois a função hash espera uma 
    # entrada em formato de bytes.
    texto_bytes = texto.encode()

    # A função sha256() é chamada para criar um objeto hash.
    objeto_hash = hashlib.sha256(texto_bytes)

    # O método hexdigest() é usado para obter a representação 
    # hexadecimal do hash.
    hash_md5_saida = objeto_hash.hexdigest()

    if hash_md5_entrada == hash_md5_saida:
        print(VERDE + '!!! VALOR HASH SHA-256 VALIDADO COM SUCESSO !!!')
    else:
        print(VERMELHO + '!!! ERRO AO VALIDAR VALOR HASH SHA-256 !!!')


#
# Execução principal do programa
#
while True:
    limpa_tela()

    print(RESET)
    print('\nVERIFICA VALOR HASH v1.0.0')
    print('---------------------------\n')

    print('1 - Verifica valor HASH MD5')
    print('2 - Verifica valor HASH SHA-1')
    print('3 - Verifica valor HASH SHA-256')
    print('4 - Sair')

    # Obtém a opção do usuário.
    opcao = input('\nDigite uma opção: ')

    # Verifica qual é a opção e chama a função apropriada.
    if opcao == '1':
        verifica_hash_md5()
    elif opcao == '2':
        verifica_hash_sha1()
    elif opcao == '3':
        verifica_hash_sha256()
    elif opcao == '4':
        print('Tchau!')
        break
    else:
        print('\nOpção inválida! Tente denovo ...')

    # Aguarda 3 segundos
    time.sleep(3)