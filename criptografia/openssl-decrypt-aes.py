#
# Exemplo para descriptografar um texto de entrada usando o 
# algoritmo AES (Advanced Encryption Standard) através 
# do utilitáro OpenSSL.
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
mensagem = input('Digite a mensagem criptografada (AES) >>> ')

# Comando shell que usa o OpenSSL para criptografar a mensagem.
comando_openssl = f'echo "{mensagem}" | openssl enc -aes-256-cbc -d -k {chave} -base64'

# Executa o comando shell.
resultado = subprocess.run(comando_openssl, shell=True, capture_output=True, text=True)

print('Texto descriptografado >>>', resultado.stdout.strip())


