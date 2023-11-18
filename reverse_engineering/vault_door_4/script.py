arr = [106, 85, 53, 116, 95, 52, 95, 98,
       0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
       0o0142, 0o0131, 0o0164, 0o063, 0o0163, 0o0137, 0o0146, 0o064,
       'a', '8', 'c', 'd', '8', 'f', '7', 'e']

answer = ''
for item in arr:
    # print(item)
    answer += item if isinstance(item, str) else chr(item)
print('picoCTF{' + answer + '}')
