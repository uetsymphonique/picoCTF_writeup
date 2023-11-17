Download file
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ wget https://artifacts.picoctf.net/c/506/asciiftw 
--2023-11-17 12:13:34--  https://artifacts.picoctf.net/c/506/asciiftw
Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 108.157.30.45, 108.157.30.81, 108.157.30.86, ...
Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|108.157.30.45|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16752 (16K) [application/octet-stream]
Saving to: ‘asciiftw’

asciiftw                                                   100%[========================================================================================================================================>]  16.36K  93.8KB/s    in 0.2s    

2023-11-17 12:13:35 (93.8 KB/s) - ‘asciiftw’ saved [16752/16752]
```
Disassemble with IDAfree
![image](https://github.com/uetsymphonique/picoCTF_writeup/assets/89717384/6545a88b-ad1b-4416-9040-99a3636be6c4)

flag:```picoCTF{ASCII_IS_EASY_3CF4BFAD}```