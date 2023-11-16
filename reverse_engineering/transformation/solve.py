flag = 'picoCTF{hahahaahahahaha}'

# print(bin(ord(flag[0])))
# print(bin(ord(flag[1])))
# print(bin(ord(flag[0]) << 8))
# print(bin((ord(flag[0]) << 8) + ord(flag[1])))
# print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))

ans = ''
with open('enc', mode='r', encoding='utf8') as f:
    enc = f.readline()
    print(enc)
    for c in enc:

        binary = bin(ord(c))[2:].rjust(16, '0')
        ans += chr(int(binary[:8], 2)) + chr(int(binary[8:], 2))
print(ans)
# picoCTF{16_bits_inst34d_of_8_0ddcd97a}

