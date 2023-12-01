Download file:
```commandline
wget https://mercury.picoctf.net/static/397a4b46a393eda0777f925f1a866f90/chall_2.S 
```
Prerequisite implementation:
```commandline
sudo apt install binutils-aarch64-linux-gnu
sudo apt install qemu-user-static
```
Compile and run the ```chall_2.S```:
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ aarch64-linux-gnu-as -o chall_2.o chall_2.S 
                                                                                                                    
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ aarch64-linux-gnu-gcc -static -o chall_2 chall_2.o
                                                                                                                    
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ ./chall_2 3297082261
Result: 1301312191
```
Convert to hexadecimal format:
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ python3                            
Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(hex(1301312191))
0x4d9072bf
```
The flag: ```picoCTF{4d9072bf}```
