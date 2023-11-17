with open('input.txt', mode='r') as input_file:
    flag = ['' for _ in range(32)]
    for line in input_file.readlines():
        char_at = int(line.split('(')[1].split(')')[0])
        char = line.split(' ')[2][1]
        # print(f'Char at {char_at} is {char}')
        flag[char_at] = char
    print('picoCTF{' + "".join(flag) + '}')
