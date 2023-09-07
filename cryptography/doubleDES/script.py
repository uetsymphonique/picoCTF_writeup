import binascii
import random
import string

from Crypto.Cipher import DES


def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad_str = block_len - over
    return (msg + " " * pad_str).encode()


def double_des(message, key1, key2):
    print('Double DES process:')
    print(f'[+]Key 1: {key1}\n[+]Key 2: {key2}')
    encryption1 = DES.new(key1, DES.MODE_ECB)
    encryption2 = DES.new(key2, DES.MODE_ECB)
    message = pad(message)
    print(f'[+]Input message: {message}')
    inner_cipher_txt = encryption1.encrypt(message)
    print(f'[+]After encryption 1: {inner_cipher_txt}')
    output_cipher_txt = encryption2.encrypt(inner_cipher_txt)
    print(f'[+]After encryption 2: {output_cipher_txt}')
    return binascii.hexlify(output_cipher_txt).decode()


def generate_key():
    return pad("".join(random.choice(string.digits) for _ in range(6)))


def des_demo():
    message = binascii.unhexlify('12345678').decode()
    key1 = b'089720  '
    key2 = b'662614  '
    cipher = double_des(message, key1, key2)
    print(f'Output: {cipher}')


def picoCTF_solve_doubleDES():
    message = binascii.unhexlify('56781222').decode()
    message = pad(message)
    cipher = binascii.unhexlify('1cdb51679c03b86b')
    encrypted_flag = binascii.unhexlify('0adbe0e029c6034655c9f81eb8032f196d7b5ebc70b5519d32f90b7c1f5f34168086daa542cdbe6f')
    print(f'Message: {message}\nCipher: {cipher}')
    KEYS = [f'{i}'.rjust(6, '0').ljust(8, ' ').encode() for i in range(999999)]
    print('Meet-in-the-middle attack:')
    look_up = dict()
    for key1 in KEYS:
        encryption1 = DES.new(key1, DES.MODE_ECB)
        look_up[encryption1.encrypt(message)] = key1
    for key2 in KEYS:
        encryption2 = DES.new(key2, DES.MODE_ECB)
        inner_cipher_txt = encryption2.decrypt(cipher)
        if inner_cipher_txt in look_up:
            print(f'[+]Key 1: {look_up[inner_cipher_txt]}\n[+]Key 2: {key2}')
            print(f'[+]After encryption 1: {inner_cipher_txt}')
            output_cipher_txt = encryption2.encrypt(inner_cipher_txt)
            print(f'[+]After encryption 2: {output_cipher_txt}')

            encryption1 = DES.new(look_up[inner_cipher_txt], DES.MODE_ECB)
            message = encryption1.decrypt(inner_cipher_txt)
            print(f'[+]Message: {binascii.hexlify(message).decode()}')
            flag = encryption1.decrypt(encryption2.decrypt(encrypted_flag))
            print(f'[+]Flag: {flag.decode().encode()}')
            break


# des_demo()
picoCTF_solve_doubleDES()
