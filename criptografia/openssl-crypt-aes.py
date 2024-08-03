#
# Exemplo para criptografar um texto de entrada usando o 
# algoritmo AES (Advanced Encryption Standard) através 
# do utilitáro OpenSSL.
#
# É necessário ter o OpenSSL instalado na máquina para 
# executar esse exemplo.
#
# Site do OpenSSL: https://openssl-library.org/
#

import os
import subprocess

# Chave Criptográfica.
chave = '012345678901234567890123456789FF'

# O algoritmo AES requer um Vetor de Inicialização (iv) com tamanho de
# 16 bytes (32 caracteres hexadecimais) para poder criptografar a
# mensagem. 
bytes_randomicos = os.urandom(32)
string_hexadecimal = bytes_randomicos.hex()

# Armazena a entrada do usuário na variável de nome mensagem.
mensagem = input('Digite uma mensagem >>> ')

# Comando shell que usa o OpenSSL para criptografar a mensagem.
comando_openssl = f'echo -n "{mensagem}" | openssl enc -aes-256-cbc -e -base64 -k {chave}'

# Executa o comando shell.
resultado = subprocess.run(comando_openssl, shell=True, capture_output=True, text=True)

print('Texto cifrado (AES) >>>', resultado.stdout.strip())


