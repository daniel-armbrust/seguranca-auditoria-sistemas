#
# Exemplo para criptografar um texto de entrada usando o 
# algoritmo DES (Data Encryption Standard) através do 
# utilitáro OpenSSL.
#
# É necessário ter o OpenSSL instalado na máquina para 
# executar esse exemplo.
#
# Site do OpenSSL: https://openssl-library.org/
#

import subprocess

# Chave Criptográfica.
chave = '012345678901234567890123456789FF'

# Armazena a entrada do usuário na variável de nome mensagem.
mensagem = input('Digite uma mensagem >>> ')

# Comando shell que usa o OpenSSL para criptografar a mensagem.
comando_openssl = f'echo -n "{mensagem}" | openssl enc -des -e -base64 -k {chave}'

# Executa o comando shell.
resultado = subprocess.run(comando_openssl, shell=True, capture_output=True, text=True)

print('Texto cifrado (DES) >>>', resultado.stdout.strip())


