I read this solution from [ARMssembly 0](https://picoctf2021.haydenhousen.com/reverse-engineering/armssembly-0) with the main idea is compiling the ```chall.S```file with the instruction from [Running ARMv8 via Linux Command Line](https://github.com/joebobmiles/ARMv8ViaLinuxCommandline)

Prerequisites:
```commandline
sudo apt install binutils-aarch64-linux-gnu
sudo apt install qemu-user-static
```
Compile and execute:
```
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ wget https://mercury.picoctf.net/static/006961dc756fc3f418b0dbe0a42dcee8/chall.S
--2023-11-21 05:30:55--  https://mercury.picoctf.net/static/006961dc756fc3f418b0dbe0a42dcee8/chall.S
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 917 [application/octet-stream]
Saving to: ‘chall.S’

chall.S                      100%[==============================================>]     917  --.-KB/s    in 0s      

2023-11-21 05:30:56 (13.7 MB/s) - ‘chall.S’ saved [917/917]

                                                                                                                    
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ aarch64-linux-gnu-as -o chall.o chall.S                                
                                                                                                                    
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ aarch64-linux-gnu-gcc -static -o chall chall.o                                  
                                                                                                                    
┌──(stupidhacker㉿kali)-[~/Downloads/pico/tmp]
└─$ ./chall 4004594377 4110761777                                                   
Result: 4110761777
```
```4110761777``` to hexadecimal representation: ```0xf5053f31```
The flag: ```picoCTF{f5053f31}```