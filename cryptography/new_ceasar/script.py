import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        # print(binary, int(binary[:4], 2), int(binary[4:], 2))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def b16_decode(cipher):
    dec = ""
    for i in range(1, len(cipher), 2):
        index1 = ord(cipher[i]) - LOWERCASE_OFFSET
        index2 = ord(cipher[i - 1]) - LOWERCASE_OFFSET
        # print(index2, index1)
        binary = "{0:04b}".format(index2) + "{0:04b}".format(index1)
        # print(binary)
        # print(chr(int(binary, 2)))
        dec += chr(int(binary, 2))
    return dec


# print("{0:08b}".format(16))


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


def is_ascii(s):
    return len(s) == len(s.encode())


enc = 'eljodmjdjcnfcdmgbleojbgngojkkdpimebgeigpdkjpmgngpfpgelemjoglghjd'

for key in ALPHABET:
    dec = ""
    for i, c in enumerate(enc):
        dec += unshift(c, key[i % len(key)])
    dec = b16_decode(dec)
    if is_ascii(dec) and " " not in dec:
        print("Flag: picoCTF{%s}" % dec.encode())
