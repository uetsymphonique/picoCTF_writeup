cipher_text = "picoCTF{w1{1wq8/7376j.:}"
tmp = ''
for i, c in enumerate(cipher_text[8:-1]):
    if i & 1 == 0:
        tmp += chr(ord(c) - 5)
    else:
        tmp += chr(ord(c) + 2)
print("picoCTF{" + tmp + "}")

