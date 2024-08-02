import hashlib

print('\nCRIA HASH > MD5')
print('---------------\n')

# 1. Abre um prompt para o usuário digitar uma linha de texto.
texto = input('Digite uma linha de texto >>> ')

# 2. A string é convertida em bytes, pois a função hash espera uma entrada em 
# formato de bytes.
texto_bytes = texto.encode()

# 3. A função md5() é chamada para criar um objeto hash.
objeto_hash = hashlib.md5(texto_bytes)

# 4. O método hexdigest() é usado para obter a representação hexadecimal 
# do hash.
hash_saida = objeto_hash.hexdigest()

# 5. O hash MD5 é gerado e impresso na tela.
print('HASH MD5:', hash_saida)