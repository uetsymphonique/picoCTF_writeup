buffer = list("jU5t_a_sna_3lpm12g94c_u_4_m7ra41")
password = ['#'] * 32

'''
for (i=0; i<8; i++) {
    buffer[i] = password.charAt(i);
}
=> buffer[0:8] = password[0:8]
'''
password[0:8] = buffer[0:8]
'''
for (; i<16; i++) {
    buffer[i] = password.charAt(23-i);
}
=> buffer[8:16] = password[15:7:-1]
=> password[8:16] = buffer[15:7:-1]
'''
password[8:16] = buffer[15:7:-1]
'''
for (; i<32; i+=2) {
    buffer[i] = password.charAt(46-i);
}
=> buffer[16:32:2] = password[30:14:-2]
=> password[16:32:2] = buffer[30:14:-2]
'''
password[16:32:2] = buffer[30:14:-2]
'''
for (i=31; i>=17; i-=2) {
    buffer[i] = password.charAt(i);
}
=> buffer[17:32:2] = password[17:32:2]
'''
password[17:32:2] = buffer[17:32:2]

print('picoCTF{' + ''.join(password) + '}')
