from Crypto.Cipher import AES #importamos la libreria AES
import hashlib
import binascii
import sys
import requests


FLAG = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
FLAG_hex = FLAG.json()["ciphertext"] #texto cifrado en hexadecimal

def decrypt():

    # /usr/share/dict/words from
    # https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
    with open("/usr/share/dict/words") as f:
        for KEY in f: 
            KEY = KEY.strip()
            KEY_main = hashlib.md5(KEY.encode()).hexdigest() #se codifica la palabra en hexadecimal

            ciphertext = bytes.fromhex(FLAG_hex)
            key = bytes.fromhex(KEY_main)
            cipher = AES.new(key, AES.MODE_ECB) #ciframos con AES en modo Electronic Code Book

            try:
                decrypted = cipher.decrypt(ciphertext)
                FLAG = binascii.unhexlify(decrypted.hex())
                if FLAG.startswith('crypto{'.encode()):
                    print('key is: %s'  % KEY)
                    print("result: ", FLAG.decode('utf-8'))
                    sys.exit(0)
            except ValueError as e:
                print("Error: ", e)
                sys.exit(1)


print(decrypt())

    