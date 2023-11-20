ans = ''
tmp = 1096770097
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

tmp = 1952395366
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

tmp = 1600270708
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

tmp = 1601398833
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

tmp = 1716808014
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

tmp = 1734293296
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

tmp = 842413104
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

tmp = 1684157793
hex_string = hex(tmp)[2:].rjust(8, '0')
for i in range(0, 8, 2):
    ans += chr(int(hex_string[i:i + 2], 16))

print('picoCTF{' + ans + '}')
