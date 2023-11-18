with open('decompile.java', mode='r') as decompiled_file:
    ans = ''
    for line in decompiled_file.readlines()[16:17 + 33 * 4:4]:
        ans = line.strip().split("\'")[1] + ans
    print(ans)